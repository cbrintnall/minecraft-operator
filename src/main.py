import kopf
import yaml
import kubernetes

@kopf.on.create("arc.com", "v1alpha1", "server")
def create_server(body, spec, **kwargs):
    raise kopf.HandlerFatalError(f"The body looks like {body}")

    return {message: "Ok"}

def create_server_body():
    return {}

def create_server_nodeport():
    return {}
