from asdTools.Classes.Tool.Counter import CounterLoop
from asdTools.Classes.Doc.DocxBase import DocxBase


class DocReader(DocxBase):
    def __init__(self, files:list=None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.docs = files
        self.docs_info = {}
        self.empty_item = {
            "path": "",
            "name": "Empty item",
            "type": "",
            "content": "",
        }
        if self.docs != None:
            self.fliter_doc()
            for doc in self.docs:
                self.docs_info[doc] = {
                    "path": doc,
                    "name": self.get_name_of_file(doc, True),
                    "type": self.get_ext_of_file(doc),
                    "content": "",
                }
            self.counter = CounterLoop(self.docs_info, self.docs, 0, self.empty_item)

    def previous_doc(self, step:int):
        res = self.counter.previous(step)
        return res
        
    def fliter_doc(self):
        docs = []
        for i, doc in enumerate(self.docs):
            docx_path = doc
            if self.check_ext(docx_path, ["docx", "doc", "pdf"]):
                docs.append(docx_path)
            else:
                continue

    def init_docs(self, files:list):
        self.docs = files
        self.docs_info = {}
        if self.docs != None:
            self.fliter_doc()
            for doc in self.docs:
                self.docs_info[doc] = {
                    "path": doc,
                    "name": self.get_name_of_file(doc, True),
                    "type": self.get_ext_of_file(doc),
                    "content": "",
                }
            self.counter = CounterLoop(self.docs_info, self.docs, 0, self.empty_item)

    def next_doc(self, step:int):
        res = self.counter.next(step)
        return res
        