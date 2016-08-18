from sru.support.web import Response
import pip_shim as pip
from sru.support.data_process import encode
import logging

log = logging.getLogger(__name__)

def get_all(**kwargs):
    packages = pip.get_all()
    if packages:
        output = encode(packages, json=True)
        return Response(body=output, content_type="application/json")
    else:
        output = encode({}, json=True)
        return Response(body=output, content_type="application/json")

def get_by_name(**kwargs):
    if "name" in kwargs:
        kwargs.setdefault("partial", False)
        kwargs.setdefault("start", False)
        kwargs.setdefault("end", False)
        if kwargs["partial"] is True:
            if kwargs["start"] is True:
                packages = pip.get_by_name(kwargs["name"], partial=True, start=True)
            elif kwargs["end"] is True:
                packages = pip.get_by_name(kwargs["name"], partial=True, end=True)
            else:
                packages = pip.get_by_name(kwargs["name"], partial=True)
        else:
            packages = pip.get_by_name(kwargs["name"])

        if packages:
            output = encode(packages, json=True)
        else:
            output = encode({}, json=True)

        return Response(body=output, content_type="application/json")
    else:
        pass
        # fail the test no name found

def install(**kwargs):
    if "name" in kwargs:
        result = pip.install(kwargs["name"])

        output = encode(result, json=True)
        return Response(body=output, content_type="application/json")
    else:
        pass
        # fail no name found

def uninstall(**kwargs):
    if "name" in kwargs:
        result = pip.uninstall(kwargs["name"])

        output = encode(result, json=True)
        return Response(body=output, content_type="application/json")
    else:
        pass
        # fail no name found