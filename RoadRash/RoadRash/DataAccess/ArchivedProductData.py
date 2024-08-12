from sqlalchemy import Column, String, DateTime, Numeric, Integer, Text, JSON, ARRAY, text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ArchivedProductData(Base):
    __tablename__ = 'archived_product_data'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    source = Column(String(50), nullable=False)
    product_id = Column(String(100), nullable=False)
    name = Column(Text)
    price = Column(Numeric(10, 2))
    description = Column(Text)
    seller = Column(String(100))
    category = Column(Text)
    image_urls = Column(ARRAY(Text))
    reviews_count = Column(Integer)
    average_rating = Column(Numeric(3, 2))
    other_details = Column(JSON)
    archived_at = Column(DateTime, default=func.now())