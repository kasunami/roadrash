from sqlalchemy import Column, String, DateTime, JSON, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class RawProductData(Base):
    __tablename__ = 'raw_product_data'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    source = Column(String(50), nullable=False)
    product_id = Column(String(100), nullable=False)
    scraped_at = Column(DateTime, default=func.now())
    raw_data = Column(JSON)