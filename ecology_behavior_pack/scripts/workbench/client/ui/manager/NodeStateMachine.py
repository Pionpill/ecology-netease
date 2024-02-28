"""
UI节点状态转换工具
(node1) ---[edge1, edge2...] --> (node2)
        \--[edgeA, edgeB...] --> (node3)
node1 接收一个 eventType，遍历 edge 列表，走首条满足条件的路径
"""
from scripts.common import logger

class NodeState(object):
    """节点状态"""
    Idle = 1        # 闲置
    Select = 2      # 选中
    UnSelect = 3    # 取消选择
    Swap = 4        # 交换
    KeepSelect = 5          # 持续选中
    KeepSelectComplete = 6  # 持续选中完成
    KeepSelectCancel = 7    # 持续选中结束
    DropAll = 8     # 丢弃  TODO 暂不实现这个功能
    Coalesce = 9    # 合并

class Node(object):
    """节点"""
    def __init__(self, onEnter, onExit):
        # type: (function, function) -> None
        object.__init__(self)
        self.onEnter = onEnter
        self.onExit = onExit

    def OnEnter(self, path):
        if self.onEnter:
            self.onEnter(path)

    def OnExit(self, path):
        if self.onExit:
            self.onExit(path)

class EventType(object):
    """玩家操作按钮类型"""
    Clicked = 0     # 点击
    Pressed = 1     # 按下
    Released = 2    # 按下后放手
    DoubleClick = 3 # 双击

class Edge(object):
    """按钮状态转换"""
    def __init__(self, tarNodeState, requirement, priority):
        # type: (int, function, int) -> None
        object.__init__(self)
        self.requirement = requirement
        self.tarNodeState = tarNodeState
        self.priority = priority

    def Require(self, path, eventType):
        # type: (str, int) -> bool
        """判断能否状态转换"""
        return self.requirement(path, eventType) if self.requirement else False

class NodeStateMachine(object):
    """
    节点状态转换管理类
    有两个重要的容器，键都是 NodeState，其中 nodes 存储节点，edges 存储节点状态改变路径
    通过 ReceiveEvent 方法接收一个 EventType 类型的事件，遍历当前节点对应的 edge 列表尝试改变状态
    每次改变状态都会调用 Node 改变前状态的 OnExit 方法和改变后状态的 OnEnter 方法
    """
    def __init__(self):
        object.__init__(self)
        self.currentNode = None
        self.currentNodeState = None
        self.defaultNodeState = NodeState.Idle
        self.__nodes = {}     # key: NodeState value: Node
        self.__edges = {}     # key: NodeState value: list[Edge]

    def AddNode(self, nodeState, onEnter=None, onExit=None):
        # type: (int, function, function) -> None
        """
        加入节点(同一种节点仅能加入一次)
        首次加入的节点会被当做当前节点
        """
        if self.__nodes.get(nodeState) is not None:
            logger.error("已注册相同状态的 node，请勿重复注册")
            return
        
        node = Node(onEnter, onExit)
        self.__nodes[nodeState] = node
        self.__edges[nodeState] = []

        if self.currentNodeState is None:
            self.currentNode = node
            self.currentNodeState = nodeState

    def AddEdge(self, oriNodeState, tarNodeState, requirement=None, priority=0):
        # type: (int, int, function, int) -> None
        """加入状态转移路径，不传 requirement 表示无条件通过"""
        edges = self.__edges.get(oriNodeState)
        if not isinstance(edges, list):
            logger.error("请先加入节点: " + oriNodeState)
            return
        
        targetIndex = -1
        for i in range(len(edges)):
            if edges[i].priority < priority:
                targetIndex = i
        edges.append(Edge(tarNodeState, requirement, priority)) if targetIndex == -1 else edges.insert(targetIndex, Edge(tarNodeState, requirement, priority))

    def ReceiveEvent(self, path, eventType):
        # type: (int, str) -> None
        """接收按钮事件"""
        edges = self.__edges.get(self.currentNodeState)
        if not edges:
            return
        for edge in edges:
            # 任意一个条件满足即改变状态
            if edge.Require(path, eventType):
                self.__ChangeState(edge.tarNodeState, path)
                break

    def SetCurrentNode(self, nodeState, onEnter=None, onExit=None):
        """设置当前节点及状态，默认 AddNode 第一次被调用的状态为当前状态"""
        node = Node(onEnter, onExit)
        self.currentNode = node
        self.currentNodeState = nodeState

    def ResetToDefault(self, path = None):
        """回归默认状态"""
        if self.currentNodeState != self.defaultNodeState:
            self.__ChangeState(self.defaultNodeState, path)

    def IsCurrentNodeState(self, nodeState):
        """判断是否为当前节点状态"""
        return self.currentNodeState == nodeState

    def __ChangeState(self, tarNodeState, path=None):
        # type: (int, str) -> None
        """每次改变状态都会调用 Node 改变前状态的 OnExit 方法和改变后状态的 OnEnter 方法"""
        node = self.__nodes.get(tarNodeState)
        if not node:
            logger.error("目标转换状态不存在!")
        self.currentNode.OnExit(path)
        self.currentNodeState = tarNodeState
        self.currentNode = self.__nodes[tarNodeState]
        self.currentNode.OnEnter(path)