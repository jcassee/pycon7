import json
import re


def to_dict(value, attr):
    return {elem[attr]: elem for elem in value}


def result_item(value, item):
    for elem in value['results']:
        if elem['item'] == item:
            return elem


def docker_container_names(containers):
    return list(set(c['docker_name'][1:] for c in containers.values()))


def failed_except_image_not_found(result, missing_ok=False):
    # Do not fail if the module did not fail
    if not result.get('failed', False):
        return False

    # Do not fail if the image was not found
    if missing_ok:
        for change in result.get('changes', []):
            data = json.loads(change)
            error = data.get('error', '')
            if re.search(r'^Error: image \S+ not found$', error):
                return False
            if re.search(r'^Tag \S+ not found in repository \S+$', error):
                return False

    return True


def any_failed_except_image_not_found(loop_result, missing_ok=False):
    if not loop_result:
        return False
    return any(failed_except_image_not_found(result, missing_ok)
                for result in loop_result.get('results', []))


class FilterModule(object):
    def filters(self):
        return {
            'to_dict': to_dict,
            'result_item': result_item,
            'docker_container_names': docker_container_names,
            'failed_except_image_not_found': failed_except_image_not_found,
            'any_failed_except_image_not_found':
                    any_failed_except_image_not_found,
        }
