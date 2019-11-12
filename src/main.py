import kopf
import yaml
import kubernetes

from kubernetes import client
from factories import server, proxy
from kubernetes.client.apis import core_v1_api
from kubernetes.client.rest import ApiException

corev1 = core_v1_api.CoreV1Api()

@kopf.on.create("arc.com", "v1alpha1", "servers")
def create_server(meta, spec, logger, namespace, **kwargs):
    to_own = []
    name = meta.get('name')
    body = server.create_server_body(name)

    if not pod_exists(name, namespace):
        obj = corev1.create_namespaced_pod(namespace=namespace, body=body)
        logger.info(f"Successfully created server {name}")
        to_own.append(obj)
    else:
        logger.info(f"Pod {name} already exists")

    service = server.create_server_nodeport(name)
    if spec.get('open', False) and not service_exists(name, namespace):
        obj = corev1.create_namespaced_service(namespace=namespace, body=service)
        logger.info(f"Successfully created service {name}")
        to_own.append(obj)
    else:
        logger.info(f"Service {name} already exists")

    # Adopt the sub-objects for cascaded deletion
    kopf.adopt(to_own)
    return {"message": "Ok"}

# TODO: This doesn't work, make it by label
def pod_exists(name: str, namespace: str) -> bool:
    try:
        _ = corev1.read_namespaced_pod(name=name, namespace=namespace)
        return True
    except ApiException as e:
        return False

    return False

def service_exists(name: str, namespace: str) -> bool:
    try:
        _ = corev1.read_namespaced_service(name=name, namespace=namespace)
        return True
    except ApiException as e:
        return False

    return False

@kopf.on.create("arc.com", "v1alpha1", "proxies")
def create_proxy(meta, logger, namespace, **kwargs):
    name = meta.get('name')
    delete_options = client.V1DeleteOptions()

    if pod_exists(name, namespace):
        response = corev1.delete_namespaced_pod(name=name, namespace=namespace, body=delete_options)
        logger.info(f"Successfully deleted server {name}")
    else:
        logger.info(f"Pod {name} doesn't exist.")

    return {"message": "Ok"}
