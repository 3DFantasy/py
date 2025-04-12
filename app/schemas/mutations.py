import strawberry


@strawberry.type
class Test:
    job_id: str
    job_queue: str


@strawberry.type
class Mutation:

    @strawberry.field
    def test(
        self,
        info: strawberry.Info,
    ) -> Test:
        print("test")
