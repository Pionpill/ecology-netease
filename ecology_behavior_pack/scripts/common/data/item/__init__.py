from scripts.common.data.item.crops.crop import CORN, WHEAT_PLANT, RICE_PLANT, SOY_BEAN, RED_BEAN, GREEN_BEAN, POTATO, SWEET_POTATO, PEANUT, TARO, YAM, SORGHUM
from scripts.common.data.item.crops.fruit import SUGARCANE, STRAWBERRY
from scripts.common.data.item.crops.fungi import LENTINULA, BUTTON_MUSHROOM, DICTYOPHORA, ENOKI, MATSUTAKE, WOOD_EAR
from scripts.common.data.item.crops.spices import CHILI, HERB, GARLIC, GINGER, SCALLION
from scripts.common.data.item.crops.vegetable import EGGPLANT, LETTUCE, ONION, TOMATO, BOK_CHOY, BROCCOLI, WHITE_BROCCOLI, CABBAGE, WHITE_CABBAGE, CARROT, WHITE_CARROT, CELERY, LEEK, PEA, PEPPER, RAPE_SEEDS, SPINACH, BEET_ROOT, BEET_LEAF

from scripts.common.data.item.materials.fuel import STRAW
from scripts.common.data.item.materials.ore import SALT
from scripts.common.data.item.materials.product import BUTTER, COOKING_OIL, DOUGH, FLOUR, GROUND_PORK, NOODLE, SALAD, STARCH, TOFU, RICE, WHEAT
from scripts.common.data.item.materials.spices import CHILI_POWDER, SEASONING, SUGAR

from scripts.common.data.item.food.vanilla import COD, SALMON, TROPICAL, COOKED_SALMON, COOKED_COD, COOKED_TROPICAL
from scripts.common.data.item.food.simple import CHEESE, BREAD, BUNS, RAW_BUNS, COOKED_RICE, MANTOU, SAUSAGE, RAW_SAUSAGE, SWEET_MILK, BEEF_PATTIES, RAW_BEEF_PATTIES
from scripts.common.data.item.food.porridge import PORRIDGE, GREEN_BEAN_PORRIDGE, RED_BEAN_PORRIDGE, SWEET_POTATO_PORRIDGE, VEGETABLE_PORRIDGE, SORGHUM_PORRIDGE, SWEET_POTATO_YAM_PORRIDGE, VEGETABLE_PORK_PORRIDGE, RED_BEAN_TARO_PORRIDGE, CORN_PEA_PORRIDGE, YAM_FISH_PORRIDGE, LENTINULA_SAUSAGE_PORRIDGE, TOMATO_BEEF_PORRIDGE, BROCCOLI_PORRIDGE
from scripts.common.data.item.food.pie import RAW_APPLE_PIE, APPLE_PIE, RAW_CORN_PIE, CORN_PIE, RAW_CHEESE_PIE, CHEESE_PIE
from scripts.common.data.item.food.fast import FRIES, BURGER_SIMPLE, BURGER, HOT_DOG
from scripts.common.data.item.food.fry import MAPO_TOFU
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
    "ham:raw_corn_pie": RAW_CORN_PIE,
    "ham:corn_pie": CORN_PIE,
    "ham:raw_cheese_pie": RAW_CHEESE_PIE,
    "ham:cheese_pie": CHEESE_PIE,
    "ham:beef_patties": BEEF_PATTIES,
    "ham:raw_beef_patties": RAW_BEEF_PATTIES,

    "ham:fries": FRIES,
    "ham:burger_simple": BURGER_SIMPLE,
    "ham:burger": BURGER,
    "ham:hot_dog": HOT_DOG,

    "ham:mapo_tofu": MAPO_TOFU,

    "ham:plain_noodles": PLAIN_NOODLES,
    "ham:pork_sauce_noodles": PORK_SAUCE_NOODLES,
    "ham:tomato_egg_noodles": TOMATO_EGG_NOODLES,

    "ham:egg_fired_rice": EGG_FIRED_RICE,
    "ham:pork_sauce_rice": PORK_SAUCE_RICE,
    "ham:yangzhou_fried_rice": YANGZHOU_FRIED_RICE
}