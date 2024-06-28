from pydantic import BaseModel
from pydantic.class_validators import Optional


class PackageInfo(BaseModel):
    # TODO: Append all desired information
    order_id: int
    time_stamp: Optional[str]

    def to_dict(self):
        return {
            # TODO: Append all desired information
            "order_id": self.order_id,
            "time_stamp": self.time_stamp
        }
