import kopf
import yaml
import kubernetes

@kopf.on.create("arc.com", "v1alpha1", "servers")
def create_server(body, spec, **kwargs):
    raise kopf.HandlerFatalError(f"The body looks like {body}")

    return {message: "Ok"}

@kopf.on.create("arc.com", "v1alpha1", "proxies")
def create_proxy(body, spec, **kwargs):
    pass

def create_server_body():
    return {}

def create_server_nodeport():
    return {}
