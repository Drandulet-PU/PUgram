from shema import async_session
from shema import User, Problem, Review
from sqlalchemy import select, desc

async def set_user(tg_id: int):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.id1 == tg_id))

        if not user:
            session.add(User(id1=tg_id))
            await session.commit()
            
async def set_review(tg_id: int, text: str):
    async with async_session() as session:
        new_review = Review(id1=tg_id, text=text)
        session.add(new_review)
        await session.flush()
        new_review = new_review.id3
        await session.commit()
        
    return new_review
        
async def get_review(tg_id: int):
    async with async_session() as session:
        return await session.scalar(select(Review).where(Review.id1 == tg_id).order_by(desc(Review.id3)).limit(1))
        