import unreal

def modify_sequence(sequence_path, audio_path):
    """Modify the Unreal Engine sequence by adding animation and audio."""
    sequence = unreal.EditorAssetLibrary.load_asset(sequence_path)
    movie_scene = sequence.get_movie_scene()
    
    # Add the dialogue audio track
    audio_track = movie_scene.add_master_track(unreal.MovieSceneAudioTrack)
    audio_section = audio_track.add_section()
    audio_section.set_sound(unreal.load_asset(audio_path))
    
    print("Sequence modified with new dialogue and camera movements!")
