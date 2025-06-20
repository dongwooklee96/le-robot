# Copyright 2025 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass, field

from lerobot.common.cameras import CameraConfig

from ..config import RobotConfig

from pathlib import Path


@dataclass(kw_only=True)
class BimanualSO101FollowerArmConfig():
    # Allows to distinguish between different robots of the same type
    id: str | None = None
    # Directory to store calibration file
    calibration_dir: Path | None = None

    # Port to connect to the arm
    port: str

    disable_torque_on_disconnect: bool = True

    # `max_relative_target` limits the magnitude of the relative positional target vector for safety purposes.
    # Set this to a positive scalar to have the same value for all motors, or a list that is the same length as
    # the number of motors in your follower arms.
    max_relative_target: int | None = None

    # Set to `True` for backward compatibility with previous policies/dataset
    use_degrees: bool = False

    cameras: dict[str, CameraConfig] = field(default_factory=dict)

@RobotConfig.register_subclass("bimanual_so101_follower")
@dataclass
class BimanualSO101FollowerConfig(RobotConfig):
    left_arm: BimanualSO101FollowerArmConfig = field(default_factory=lambda: BimanualSO101FollowerArmConfig(port="/dev/ttyUSB0"))
    right_arm: BimanualSO101FollowerArmConfig = field(default_factory=lambda: BimanualSO101FollowerArmConfig(port="/dev/ttyUSB1"))
    cameras: dict[str, CameraConfig] = field(default_factory=dict)