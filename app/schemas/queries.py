import strawberry
from typing import Optional
from prisma import Prisma


@strawberry.type
class Test:
    job_id: Optional[str]
    job_queue: Optional[str]



@strawberry.type
class Query:
    @strawberry.field
    async def is_up(self) -> bool:
        prisma = Prisma()
        await prisma.connect()

        account = await prisma.account.find_unique({
            'email':"wilsonbirch@gmail.com"
        })
        
        await prisma.disconnect()
        if(account):
          return True
        else:
          return False
