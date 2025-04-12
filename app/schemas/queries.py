import strawberry
from typing import Optional



@strawberry.type
class Test:
    job_id: Optional[str]
    job_queue: Optional[str]



@strawberry.type
class Query:
    @strawberry.field
    async def is_up(self) -> bool:

        print(f"isUp")
        return True
