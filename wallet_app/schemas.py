import uuid
from datetime import datetime
from locale import currency
from typing import Optional
from pydantic import BaseModel

class DepositSuperPaySchema(BaseModel):
    description: str
    amount: float
    currency: str
    redirect_success_url: str
    redirect_failure_url: str
    locale: str
    merchant_id: uuid

class PayoutSuperPaySchema(BaseModel):
    currency: str
    amount: float
    merchant_id: uuid
    operation_time: int
    operation_success: bool
    operation_description: str

class StatusSuperPaySchema(BaseModel):
    merchant_id: uuid
    operation_time: int
    operation_success: bool
    operation_description: str


class CallbackMetaSchema(BaseModel):
    total: int
    pages: int
    page: int

class CallbackSuperPaySchema(BaseModel):
    meta: CallbackMetaSchema
    id: uuid
    status: str
    status_detail: str
    attempt: int
    max_attempt: int
    created: int
    progresses: int
