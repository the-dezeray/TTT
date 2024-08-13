"""module contains note class"""

class Note():
    """_summary_
    """  
    def __init__(self,type :str= None,deadline :str =None,content :str =None,parent:str = None) -> None:
        """note object

        Args:
            type (str, optional):each note has a type ["task","sprint"] and more a. Defaults to None.
            deadline (str, optional): _description_. Defaults to None.
            content (str, optional): _description_. Defaults to None.
        """
        self.type = type
        self.id = None
        self.content =  content
        self.created_time = self.get_current_time()
        self.deadline= deadline

    def get_current_time():
        return 0
