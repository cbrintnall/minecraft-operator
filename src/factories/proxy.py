
BUNGEE_IMAGE = "quay.io/cbrintnall/bungeecord"

def create_proxy_body(name: str) -> dict:
    return {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {
            "type": "proxy",
            "name": f"{name}",
            "labels": {
                "owner": name
            }
        },
        "spec": {
            "containers": [
                {
                    "image": BUNGEE_IMAGE,
                    "name": "bungee"
                }
                # TODO: Add RCON handling container?
            ]
        }
    }
