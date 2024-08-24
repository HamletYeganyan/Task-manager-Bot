from sqlalchemy import text, select
from src.database import async_engine, async_session_factory
from src.models import UserORM, TaskORM
import asyncio

@staticmethod
async def Session_func(new_data):
    async with async_session_factory() as session:
        session.add(new_data)
        await session.commit()

@staticmethod
async def insert_data_user(user_id, username, first_name, last_name, created_at, updated_at, task_count=0, completed_task_count=0, incomplete_task_count=0, last_task_created=None, last_task_updated=None):
    new_data = UserORM(
        user_id=user_id,
        username=username,
        first_name=first_name,
        last_name=last_name,
        created_at=created_at,
        updated_at=updated_at,
        task_count=task_count,
        completed_task_count=completed_task_count,
        incomplete_task_count=incomplete_task_count,
        last_task_created=last_task_created,
        last_task_updated=last_task_updated
    )
    await Session_func(new_data)

@staticmethod
async def insert_data_task(user_id, task_id, description, deadline, is_completed, created_at, updated_at):
    new_data = TaskORM(
        user_id=user_id,
        task_id=task_id,
        description=description,
        deadline=deadline,
        is_completed=is_completed,
        created_at=created_at,
        updated_at=updated_at
    )
    await Session_func(new_data)

@staticmethod
async def select_one_item(table_orm, prim_key):
    '''example table_orm=UserORM or TaskORM'''
    async with async_session_factory() as session:
        item = await session.get(table_orm, prim_key)
        return item

@staticmethod
async def select_column_items(table_orm, column_name):
    async with async_session_factory() as session:
        query = select(getattr(table_orm, column_name))
        result = await session.execute(query)
        return result.scalars().all()

@staticmethod
async def update_table_object(table_orm, column_name, prim_id, new_data):
    async with async_session_factory() as session:
        stmt = (
            text(f'UPDATE "{table_orm.__tablename__}" SET "{column_name}" = :new_data WHERE id = :prim_id')
        )
        await session.execute(stmt, {'new_data': new_data, 'prim_id': prim_id})
        await session.commit()
async def insert_data_to_tables(table_name, ready_info_dict):
    if table_name == "user":
        await insert_data_user(
            user_id=ready_info_dict["user_id"],
            username=ready_info_dict["username"],
            first_name=ready_info_dict["first_name"],
            last_name=ready_info_dict["last_name"],
            created_at=ready_info_dict["created_at"],
            updated_at=ready_info_dict["updated_at"],
            task_count=ready_info_dict["task_count"],
            completed_task_count=ready_info_dict["completed_task_count"],
            incomplete_task_count=ready_info_dict["incomplete_task_count"],
            last_task_created=ready_info_dict["last_task_created"],
            last_task_updated=ready_info_dict["last_task_updated"]
        )
    elif table_name=='task':
        await insert_data_task(
            task_id=ready_info_dict["task_id"],
            user_id=ready_info_dict["user_id"],
            description=ready_info_dict["description"],
            deadline=ready_info_dict["deadline"],
            is_completed=ready_info_dict["is_completed"],
            created_at=ready_info_dict["created_at"],
            updated_at=ready_info_dict["updated_at"]
        )