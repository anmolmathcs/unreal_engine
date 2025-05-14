def apply_lipsync(sequence, audio_path):
    """Apply lipsync animation to the character based on the audio file."""
    metahuman_actor = unreal.find_actor_by_name("MyMetahuman")
    lipsync_anim = unreal.MetahumanSDK.generate_lipsync(audio_path)
    metahuman_actor.apply_animation(lipsync_anim)
    print("Lipsync applied successfully!")
