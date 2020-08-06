import networkx as nx
import jira
from configuration import Configuration
from itertools import chain
from typing import (
    List
)


class BaseIssueNode:
    pass


class IssuesContainer:
    """Container containing lists of code representation of real Jira issues."""
    def __init__(self, fetched_issues):
        self.epics = []
        self.tasks = []
        self.subtasks = []
        self._build(fetched_issues)

    def _build(self, fetched_issues: List[jira.Issue]):
        pass

    def all_issues(self) -> chain:
        return chain(self.epics, self.tasks, self.subtasks)


class IssuesDirectedGraph(nx.DiGraph):
    """Directed Graph representation of the Issues Graph on Jira project."""
    def __init__(self, fetched_issues):
        super().__init__()
        self.config = Configuration()
        self._build(fetched_issues)

    def _build(self, fetched_issues: List[jira.Issue]) -> None:
        issues_container = IssuesContainer(fetched_issues)
        self._add_all_nodes(issues_container.all_issues())

    def _add_all_nodes(self, issues: chain) -> None:
        for issue in issues:
            self.add_node(issue)
