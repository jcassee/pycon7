from itertools import chain

import github3


project_cache = {}


def development_containers(templates, github_token=None, cache=True):
    github = github3.login(token=github_token)
    return list(chain.from_iterable(project_containers(template, github, cache)
                for template in templates))


def project_containers(template, github, cache):
    tags = project_tags(template['project'], github, cache)
    return [container(template, tag) for tag in tags]


def container(template, tag):
    domain = '%s-%s.%s' % (template['name_base'], tag, template['domain_base'])
    env = template.get('env', {})
    env['WEB_DOMAIN'] = domain 

    return {
        'name': '%s_%s' % (template['name_base'], tag),
        'image': '%s:%s' % (template['image_repo'], tag),
        'missing_ok': True,
        'env': env,
        'vars': template.get('vars', {}),
    }


def project_tags(project, github, cache):
    if cache and project in project_cache:
        return project_cache[project]
    owner, repo_name = project.split('/', 1)
    repo = github.repository(owner, repo_name)
    pull_requests = ('pr%d' % b.number for b in repo.pull_requests())
    result = sorted(pull_requests)
    project_cache[project] = result
    return result


class FilterModule(object):
    def filters(self):
        return {
            'development_containers': development_containers,
        }
