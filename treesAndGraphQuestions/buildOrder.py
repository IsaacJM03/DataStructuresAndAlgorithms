def create_graph(projects,dependencies):
  project_graph = {}
  for project in projects:
    project_graph[project] = []
  for pairs in dependencies:
    project_graph[pairs[0]].extend([pairs[1]])
  return project_graph

def get_projects_with_dependencies(graph):
  projects_with_dependencies = set()
  for project in graph:
    # adding values to graph dictionary since values are dependent on key
    projects_with_dependencies = projects_with_dependencies.union(set(graph[project])) # merging the set, to show the dependencies

  return projects_with_dependencies

def get_projects_without_dependencies(projects_with_dependencies,graph):
  projects_without_dependencies = set()
  for project in graph:
    if project not in projects_with_dependencies:
      projects_without_dependencies.add(project)
  return projects_without_dependencies

def build_order(projects,dependencies):
  build_order = []
  project_graph = create_graph(projects,dependencies)
  while project_graph:
    print(project_graph)
    projects_with_dependencies = get_projects_with_dependencies(project_graph)
    projects_without_dependencies = get_projects_without_dependencies(projects_with_dependencies,project_graph)
    print(projects_without_dependencies)
    if len(projects_without_dependencies) == 0 and project_graph: # is not empty
      raise ValueError("There is a cycle in the build order")
    for independent_project in projects_without_dependencies:
      build_order.append(independent_project)
      del project_graph[independent_project]
  return build_order

graph = create_graph(['A','B','C','D','E','F','G'],[('A','D'),('F','B'),('F','A'),('F','C'),('F','E'),('D','B'),('D','C'),('D','E'),('B','G'),('C','G'),('E','G')])

dependents = get_projects_with_dependencies(graph)

notDependents = get_projects_without_dependencies(dependents,graph)

print(build_order(['A','B','C','D','E','F','G'],[('A','D'),('F','B'),('F','A'),('F','C'),('F','E'),('D','B'),('D','C'),('D','E'),('B','G'),('C','G'),('E','G')]))