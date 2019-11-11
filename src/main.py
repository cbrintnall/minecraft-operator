import kopf
import yaml
import kubernetes

from factories import server, proxy
from kubernetes.client.apis import core_v1_api

corev1 = core_v1_api.CoreV1Api()

@kopf.on.create("arc.com", "v1alpha1", "servers")
def create_server(meta, spec, logger, namespace, **kwargs):
    body = server.create_server_body(meta.get('name'))
    obj = corev1.create_namedspaced_pod(namespace=namespace, body=body)

    logger.info(f"Successfully created server {meta.get('name')}")

    return {message: "Ok"}

@kopf.on.create("arc.com", "v1alpha1", "proxies")
def create_proxy(body, spec, **kwargs):
    pass
