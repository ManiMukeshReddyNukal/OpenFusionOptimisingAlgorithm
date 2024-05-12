class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.schema={name:defaultdict(list) for name in names}
        self.lastids=defaultdict()

    def insertRow(self, name: str, row: List[str]) -> None:
        lastid=1
        if name in self.lastids.keys():
            lastid=self.lastids[name]   
        self.schema[name][lastid]=row
        self.lastids[name]=lastid+1
    def deleteRow(self, name: str, rowId: int) -> None:
        del self.schema[name][rowId]

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.schema[name][rowId][columnId-1]

