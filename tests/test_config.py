import pytest

class CustomError(Exception):
    def __init__(self,message="value not in range"):
        self.message=message
        super().__init__(self.message)

def test_generic():
    a=2
    with pytest.raises(CustomError):
        if a not in range(10,20):
            raise CustomError
        