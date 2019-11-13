import uuid

SPIGOT_IMAGE = "quay.io/cbrintnall/spigot"

def create_server_body(name: str) -> dict:
    return {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {
            "type": "server",
            "name": f"{name}",
            "labels": {
                "owner": name
            }
        },
        "spec": {
            "containers": [
                {
                    "image": SPIGOT_IMAGE,
                    "name": "spigot"
                }
                # TODO: Add RCON handling container?
            ]
        }
    }

def create_server_nodeport(name: str) -> dict:
    return {
        "apiVersion": "v1",
        "kind": "Service",
        "metadata": {
            "name": name
        },
        "spec": {
            "selector": {
                "owner": name
            },
            "type": "NodePort",
            "ports": [
                {
                    "protocol": "TCP",
                    "port": 25565,
                    "targetPort": 25565
                }
            ]
        }
    }
