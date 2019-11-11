BUNGEE_IMAGE = ""
SPIGOT_IMAGE = "quay.io/cbrintnall/spigot"

def create_server_body(name: str) -> dict:
    return {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {
            "type": "server",
            "name": name
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

def create_server_nodeport():
    return {}
