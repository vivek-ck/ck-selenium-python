from src.utils.base_class import BaseClass
from src.utils import base_behave_sb
base_behave_sb.set_base_class(BaseClass)  # Accepts a BaseCase subclass
from src.utils.base_behave_sb import before_all  # noqa
from src.utils.base_behave_sb import before_feature  # noqa
from src.utils.base_behave_sb import before_scenario  # noqa
from src.utils.base_behave_sb import before_step  # noqa
from src.utils.base_behave_sb import after_step  # noqa
from src.utils.base_behave_sb import after_scenario  # noqa
from src.utils.base_behave_sb import after_feature  # noqa
from src.utils.base_behave_sb import after_all  # noqa