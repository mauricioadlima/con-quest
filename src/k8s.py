from kubernetes import client, config
from questdb import QuestDB
from os import path
import yaml


class K8s:

    def __init__(self):
        config.load_kube_config()
        self.k8s_apps_v1 = client.AppsV1Api()

    def __get_template_file(self):
        return path.join(path.dirname(__file__), "../k8s-templates/stateful-set.yaml")

    def __get_namespace(self, questdb: QuestDB):
        return 'default' if questdb.namespace is None else questdb.namespace

    def create(self, questdb: QuestDB):
        with open(self.__get_template_file()) as f:
            stateful_set = yaml.safe_load(f)
            stateful_set['metadata']['name'] = questdb.name
            self.k8s_apps_v1.create_namespaced_stateful_set(
                body=stateful_set, namespace=self.__get_namespace(questdb))

    def get_status(self, namespace: str, name: str):
        resp = self.k8s_apps_v1.read_namespaced_stateful_set_status(name, namespace)
        return 'OK' if resp.status.replicas == resp.status.ready_replicas else 'NOK'

    def delete(self, namespace: str, name: str):
        self.k8s_apps_v1.delete_namespaced_stateful_set(name, namespace)
