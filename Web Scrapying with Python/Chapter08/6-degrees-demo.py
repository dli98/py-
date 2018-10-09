class SolutionFound(RuntimeError):
    def __init__(self, message):
        self.message = message


def getLinks(fromPageId):
    data = {1: [2, 3, 4],
            2: [5, 6, 7],
            3: [8, 9, 10],
            4: [11, 12, 13],
            6: [14, 15, 16]}
    if fromPageId not in data:
        return None
    return data[fromPageId]


def constructDict(currentPageId):
    links = getLinks(currentPageId)
    if links:
        return dict(zip(links, [{}] * len(links)))
    return {}


def searchDepth(targetPageId, currentPageId, linkTree, depth):
    print('depth: ', depth)
    # print(id(linkTree))
    if depth == 0:
        return linkTree
    if not linkTree:
        linkTree = constructDict(currentPageId)
        if not linkTree:
            return {}
    if targetPageId in linkTree.keys():
        print('TAREGT: ' + str(targetPageId) + ' FOUND!')
        raise SolutionFound('PAGE:' + str(currentPageId))

    for branchkey, branchvalue in linkTree.items():
        try:
            linkTree[branchkey] = searchDepth(targetPageId, branchkey,
                                              branchvalue, depth - 1)
        except SolutionFound as e:
            print(e.message)
            raise SolutionFound('PAGE:' + str(currentPageId))
    return linkTree


try:
    linkTree = searchDepth(14, 1, {}, 4)

    print('No solution found')
except SolutionFound as e:
    print(e.message)
