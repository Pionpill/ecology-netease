from scripts.common.data.item.crops.crop import CORN, WHEAT_PLANT, RICE_PLANT, SOY_BEAN, RED_BEAN, GREEN_BEAN, POTATO, SWEET_POTATO, PEANUT, TARO, YAM, SORGHUM
from scripts.common.data.item.crops.fruit import SUGARCANE, STRAWBERRY
from scripts.common.data.item.crops.fungi import LENTINULA, BUTTON_MUSHROOM, DICTYOPHORA, ENOKI, MATSUTAKE, WOOD_EAR
from scripts.common.data.item.crops.spices import CHILI, HERB, GARLIC, GINGER, SCALLION
from scripts.common.data.item.crops.vegetable import EGGPLANT, LETTUCE, ONION, TOMATO, BOK_CHOY, BROCCOLI, WHITE_BROCCOLI, CABBAGE, WHITE_CABBAGE, CARROT, WHITE_CARROT, CELERY, LEEK, PEA, PEPPER, RAPE_SEEDS, SPINACH, BEET_ROOT, BEET_LEAF

from scripts.common.data.item.materials.fuel import STRAW
from scripts.common.data.item.materials.ore import SALT
from scripts.common.data.item.materials.product import BUTTER, COOKING_OIL, DOUGH, FLOUR, GROUND_PORK, NOODLE, SALAD, STARCH, TOFU, RICE, WHEAT
from scripts.common.data.item.materials.spices import CHILI_POWDER, SEASONING, SUGAR, SIMPLE_PACK, MEAL_PACK, TOMATO_PACK, MUSHROOM_PACK, CHILI_PACK

from scripts.common.data.item.food.vanilla import COD, SALMON, TROPICAL, COOKED_SALMON, COOKED_COD, COOKED_TROPICAL
from scripts.common.data.item.food.simple import CHEESE, BREAD, BUNS, RAW_BUNS, COOKED_RICE, MANTOU, SAUSAGE, RAW_SAUSAGE, SWEET_MILK, BEEF_PATTIES, RAW_BEEF_PATTIES
from scripts.common.data.item.food.porridge import PORRIDGE, GREEN_BEAN_PORRIDGE, RED_BEAN_PORRIDGE, SWEET_POTATO_PORRIDGE, VEGETABLE_PORRIDGE, SORGHUM_PORRIDGE, SWEET_POTATO_YAM_PORRIDGE, VEGETABLE_PORK_PORRIDGE, RED_BEAN_TARO_PORRIDGE, CORN_PEA_PORRIDGE, YAM_FISH_PORRIDGE, LENTINULA_SAUSAGE_PORRIDGE, TOMATO_BEEF_PORRIDGE, BROCCOLI_PORRIDGE
from scripts.common.data.item.food.pie import APPLE_PIE, RAW_APPLE_PIE, CARROT_PIE, RAW_CARROT_PIE, CORN_CHICKEN_PIE, RAW_CORN_CHICKEN_PIE, MUSHROOM_PORK_PIE, RAW_MUSHROOM_PORK_PIE, POTATO_BEEF_PIE, RAW_POTATO_BEEF_PIE, STRAWBERRY_PIE, RAW_STRAWBERRY_PIE, SWEET_POTATO_PIE, RAW_SWEET_POTATO_PIE, TARO_PIE, RAW_TARO_PIE, CHEESE_PIE, RAW_CHEESE_PIE, CORN_PIE, RAW_CORN_PIE
from scripts.common.data.item.food.fast import FRIES, ONION_RING, BEEF_BURGER, CHICKEN_BURGER, COD_BURGER,  DOUBLE_BEEF_BURGER, HOT_DOG
from scripts.common.data.item.food.fry import CELERY_BEEF, FRY_BOK_CHOY, FRY_BROCCOLI, FRY_CABBAGE, FRY_MATSUTAKE, GARLIC_LETTUCE, LEEK_EGG, ONION_POTATO, PEANUT_SPINACH, PEPPER_PORK, PORK_EGGPLANT, SCALLION_MUTTON, TOMATO_EGG
from scripts.common.data.item.food.noodles import PLAIN_NOODLES, PORK_SAUCE_NOODLES, TOMATO_EGG_NOODLES
from scripts.common.data.item.food.rice import EGG_FIRED_RICE, PORK_SAUCE_RICE, YANGZHOU_FRIED_RICE


ITEM_DATA = {
    "minecraft:cod": COD,
    "minecraft:cooked_cod": COOKED_COD,
    "minecraft:salmon": SALMON,
    "minecraft:cooked_salmon": COOKED_SALMON,
    "minecraft:tropical": TROPICAL,
    "minecraft:cooked_tropical": COOKED_TROPICAL,
    
    "ham:corn": CORN,
    "ham:wheat_plant": WHEAT_PLANT,
    "ham:rice_plant": RICE_PLANT,
    "ham:soy_bean": SOY_BEAN,
    "ham:red_bean": RED_BEAN,
    "ham:green_bean": GREEN_BEAN,
    "ham:potato": POTATO,
    "ham:sweet_potato": SWEET_POTATO,
    "ham:peanut": PEANUT,
    "ham:taro": TARO,
    "ham:yam": YAM,
    "ham:sorghum": SORGHUM,
    
    "ham:sugarcane": SUGARCANE,
    "ham:strawberry": STRAWBERRY,

    "ham:lentinula": LENTINULA,
    "ham:button_mushroom": BUTTON_MUSHROOM,
    "ham:dictyophora": DICTYOPHORA,
    "ham:enoki": ENOKI,
    "ham:matsutake": MATSUTAKE,
    "ham:wood_ear": WOOD_EAR,
    "ham:chili": CHILI,
    "ham:herb": HERB,
    "ham:garlic": GARLIC,
    "ham:ginger": GINGER,
    "ham:eggplant": EGGPLANT,
    "ham:lettuce": LETTUCE,
    "ham:onion": ONION,
    "ham:scallion": SCALLION,
    "ham:tomato": TOMATO,
    "ham:bok_choy": BOK_CHOY,
    "ham:white_cabbage": WHITE_CABBAGE,
    "ham:carrot": CARROT,
    "ham:white_carrot": WHITE_CARROT,
    "ham:celery": CELERY,
    "ham:leek": LEEK,
    "ham:pea": PEA,
    "ham:pepper": PEPPER,
    "ham:rape_seeds": RAPE_SEEDS,
    "ham:spinach": SPINACH,
    "ham:beet_root": BEET_ROOT,
    "ham:beet_leaf": BEET_LEAF,

    "ham:straw": STRAW,
    "ham:salt": SALT,
    "ham:butter": BUTTER,
    "ham:cooking_oil": COOKING_OIL,
    "ham:dough": DOUGH,
    "ham:flour": FLOUR,
    "ham:ground_pork": GROUND_PORK,
    "ham:noodle": NOODLE,
    "ham:salad": SALAD,
    "ham:starch": STARCH,
    "ham:tofu": TOFU,
    "ham:chili_powder": CHILI_POWDER,
    "ham:seasoning": SEASONING,
    "ham:sugar": SUGAR,
    "ham:simple_pack": SIMPLE_PACK, 
    "ham:meal_pack": MEAL_PACK, 
    "ham:tomato_pack": TOMATO_PACK, 
    "ham:mushroom_pack": MUSHROOM_PACK, 
    "ham:chili_pack": CHILI_PACK,
    "ham:rice": RICE,
    "ham:wheat": WHEAT,
    "ham:broccoli": BROCCOLI,
    "ham:white_broccoli": WHITE_BROCCOLI,
    "ham:cabbage": CABBAGE,

    "ham:cheese": CHEESE,
    "ham:bread": BREAD,
    "ham:buns": BUNS,
    "ham:raw_buns": RAW_BUNS,
    "ham:cooked_rice": COOKED_RICE,
    "ham:mantou": MANTOU,
    "ham:sausage": SAUSAGE,
    "ham:raw_sausage": RAW_SAUSAGE,
    "ham:sweet_milk": SWEET_MILK,

    "ham:porridge": PORRIDGE, 
    "ham:green_bean_porridge": GREEN_BEAN_PORRIDGE, 
    "ham:red_bean_porridge": RED_BEAN_PORRIDGE, 
    "ham:sweet_potato_porridge": SWEET_POTATO_PORRIDGE, 
    "ham:vegetable_porridge": VEGETABLE_PORRIDGE, 
    "ham:sorghum_porridge": SORGHUM_PORRIDGE, 
    "ham:sweet_potato_yam_porridge": SWEET_POTATO_YAM_PORRIDGE, 
    "ham:vegetable_pork_porridge": VEGETABLE_PORK_PORRIDGE, 
    "ham:red_bean_taro_porridge": RED_BEAN_TARO_PORRIDGE, 
    "ham:corn_pea_porridge": CORN_PEA_PORRIDGE, 
    "ham:yam_fish_porridge": YAM_FISH_PORRIDGE, 
    "ham:lentinula_sausage_porridge": LENTINULA_SAUSAGE_PORRIDGE, 
    "ham:tomato_beef_porridge": TOMATO_BEEF_PORRIDGE, 
    "ham:broccoli_porridge": BROCCOLI_PORRIDGE,

    "ham:raw_apple_pie": RAW_APPLE_PIE,
    "ham:apple_pie": APPLE_PIE,
    "ham:raw_carrot_pie": RAW_CARROT_PIE,
    "ham:carrot_pie": CARROT_PIE,
    "ham:raw_corn_chicken_pie": RAW_CORN_CHICKEN_PIE,
    "ham:corn_chicken_pie": CORN_CHICKEN_PIE,
    "ham:raw_mushroom_pork_pie": RAW_MUSHROOM_PORK_PIE,
    "ham:mushroom_pork_pie": MUSHROOM_PORK_PIE,
    "ham:raw_sweet_potato_pie": RAW_SWEET_POTATO_PIE,
    "ham:sweet_potato_pie": SWEET_POTATO_PIE,
    "ham:raw_potato_beef_pie": RAW_POTATO_BEEF_PIE,
    "ham:potato_beef_pie": POTATO_BEEF_PIE,
    "ham:raw_strawberry_pie": RAW_STRAWBERRY_PIE,
    "ham:strawberry_pie": STRAWBERRY_PIE,
    "ham:raw_taro_pie": RAW_TARO_PIE,
    "ham:taro_pie": TARO_PIE,
    "ham:raw_corn_pie": RAW_CORN_PIE,
    "ham:corn_pie": CORN_PIE,
    "ham:raw_cheese_pie": RAW_CHEESE_PIE,
    "ham:cheese_pie": CHEESE_PIE,
    "ham:beef_patties": BEEF_PATTIES,
    "ham:raw_beef_patties": RAW_BEEF_PATTIES,

    "ham:fries": FRIES,
    "ham:onion_ring": ONION_RING, 
    "ham:beef_burger": BEEF_BURGER, 
    "ham:chicken_burger": CHICKEN_BURGER, 
    "ham:cod_burger": COD_BURGER, 
    "ham:double_beef_burger": DOUBLE_BEEF_BURGER,
    "ham:hot_dog": HOT_DOG,

    "ham:celery_beef": CELERY_BEEF, 
    "ham:fry_bok_choy": FRY_BOK_CHOY, 
    "ham:fry_broccoli": FRY_BROCCOLI, 
    "ham:fry_cabbage": FRY_CABBAGE, 
    "ham:fry_matsutake": FRY_MATSUTAKE, 
    "ham:garlic_lettuce": GARLIC_LETTUCE, 
    "ham:leek_egg": LEEK_EGG, 
    "ham:onion_potato": ONION_POTATO, 
    "ham:peanut_spinach": PEANUT_SPINACH, 
    "ham:pepper_pork": PEPPER_PORK, 
    "ham:pork_eggplant": PORK_EGGPLANT, 
    "ham:scallion_mutton": SCALLION_MUTTON, 
    "ham:tomato_egg": TOMATO_EGG,

    "ham:plain_noodles": PLAIN_NOODLES,
    "ham:pork_sauce_noodles": PORK_SAUCE_NOODLES,
    "ham:tomato_egg_noodles": TOMATO_EGG_NOODLES,

    "ham:egg_fired_rice": EGG_FIRED_RICE,
    "ham:pork_sauce_rice": PORK_SAUCE_RICE,
    "ham:yangzhou_fried_rice": YANGZHOU_FRIED_RICE
}