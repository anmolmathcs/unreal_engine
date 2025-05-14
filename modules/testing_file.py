# import unreal

# # Get the Asset Registry instance
# asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()

# # Correct way to get assets by class in Unreal Engine 5.3+
# sequence_class = unreal.TopLevelAssetPath("/Script/LevelSequence.LevelSequence")

# # Get all LevelSequence assets
# sequence_assets = asset_registry.get_assets_by_class(sequence_class)

# if sequence_assets:
#     print("Found Level Sequences:")
#     for asset in sequence_assets:
#         print(asset.get_full_name())
# else:
#     print("No Level Sequences found!")


# import unreal

# asset_path = r"C:\Users\anmol\Downloads\Pepe_Pro 5.5\Pepe_Pro 5.5\Content\Main_BuiltData.uasset"  # Use the correct asset path

# # Use load_object to load the asset in UE 5.5+
# asset = unreal.load_object(None, asset_path)

# if asset:
#     print(f"Successfully loaded: {asset.get_name()}")
# else:
#     print("Failed to load asset. Check the path.")

import unreal

if unreal.EditorUtilityLibrary.get_editor_world():
    print(unreal.SystemLibrary.get_engine_version())
else:
    print("Unreal Editor is not running! Some functions may be unavailable.")

