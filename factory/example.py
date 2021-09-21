"""
Basic video exporting example
"""

import pathlib
from abc import ABC, abstractmethod


class VideoExporter(ABC):
    """Basic representation ofg video exporting codec
    """

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares video data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Export the video data to a folde

        Args:
            folder (pathlib.Path): folder path
        """


class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting codec."""

    def prepare_export(self, video_data):
        print('Preparing video data for lossless export.')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video data for lossless format to {folder}.')


class H264BPVideoExporter(VideoExporter):
    """H.264 video exporting codec with baseline profile."""


    def prepare_export(self, video_data):
        print('Preparing video data for H.264 (Baseline) export.')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video data for H.264 (Baseline) format to {folder}.')


class H264Hi422PVideoExporter(VideoExporter):
    """H2.64 video exporting codec with baseline profile."""

    def prepare_export(self, video_data):
        print('Preparing video data for H.264 (Hi422P) export.')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video data for H.264 (Hi422P) format to {folder}.')


class AudioExporter(ABC):
    """Basic representation of audio exporting codec
    """

    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepares audio data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Export the audio data to a folde

        Args:
            folder (pathlib.Path): folder path
        """


class AACAudioExporter(AudioExporter):
    """AAC audio exporting codec with baseline profile."""

    def prepare_export(self, video_data):
        print('Preparing video data for AAC export.')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video data for AAC format to {folder}.')


class WAVAudioExporter(AudioExporter):
    """WAV audio exporting codec with baseline profile."""

    def prepare_export(self, video_data):
        print('Preparing video data for WAV export.')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video data for WAV format to {folder}.')


def main() -> None:
    """Main function
    """

    # read the desired export quality
    export_quality: str
    while True:
        export_quality = input('Enter desired quality (low, high, master): ')
        if export_quality in {"low", "high", "master"}:
            break
        print(f'Unknown output quality option: {export_quality}. ')

    video_exporter: VideoExporter
    audio_exporter: AudioExporter

    if export_quality == "low":
        video_exporter = H264BPVideoExporter()
        audio_exporter = AACAudioExporter()
    elif export_quality == "high":
        video_exporter = H264Hi422PVideoExporter()
        audio_exporter = AACAudioExporter()
    elif export_quality == "master":
        video_exporter = H264BPVideoExporter()
        audio_exporter = AACAudioExporter()
    else:
        video_exporter = LosslessVideoExporter()
        audio_exporter = WAVAudioExporter()

    audio_exporter.prepare_export("placeholder)_for_audio_data")

    folder = pathlib.Path("./results")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    main()

