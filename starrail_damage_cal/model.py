from typing import List, Union

from msgspec import Struct, field


class MohomoAvatarSkill(Struct):
    skillId: int
    skillName: str
    skillEffect: str
    skillAttackType: str
    skillLevel: int


class MohomoAvatarExtraAbility(Struct):
    extraAbilityId: int
    extraAbilityLevel: int


class AttributeBounsStatusAdd(Struct):
    property_: str = field(name="property")
    name: str
    value: float


class MohomoAvatarAttributeBonus(Struct):
    attributeBonusId: int
    attributeBonusLevel: int
    statusAdd: AttributeBounsStatusAdd


class RelicMainAffix(Struct):
    AffixID: int
    Property: str
    Name: str
    Value: float


class RelicSubAffix(Struct):
    SubAffixID: int
    Property: str
    Name: str
    Cnt: int
    Step: int
    Value: float


class Relic(Struct):
    relicId: int
    relicName: str
    SetId: int
    SetName: str
    Type: int
    MainAffix: RelicMainAffix
    SubAffixList: List[RelicSubAffix]
    Level: int = 0


class AvatarBaseAttributes(Struct):
    hp: float
    attack: float
    defence: float
    CriticalChanceBase: float
    CriticalDamageBase: float
    speed: float
    BaseAggro: float


class EquipmentBaseAttributes(Struct):
    hp: float
    attack: float
    defence: float


class AvatarEquipmentInfo(Struct):
    equipmentID: int
    equipmentName: str
    equipmentLevel: int
    equipmentPromotion: int
    equipmentRank: int
    equipmentRarity: int
    baseAttributes: EquipmentBaseAttributes


class RankData(Struct):
    rankId: int
    rankName: str


class MohomoCharacter(Struct):
    uid: str
    nickName: str
    avatarId: int
    avatarName: str
    avatarElement: str
    avatarRarity: str
    avatarLevel: int
    avatarPromotion: int
    avatarSkill: List[MohomoAvatarSkill]
    avatarExtraAbility: List[MohomoAvatarExtraAbility]
    avatarAttributeBonus: List[MohomoAvatarAttributeBonus]
    RelicInfo: List[Relic]
    avatarEnName: str
    baseAttributes: AvatarBaseAttributes
    equipmentInfo: AvatarEquipmentInfo
    rank: int
    rankList: List[RankData]
