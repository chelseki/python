import pytest
from television import Television

class TestTelevision:
    def test_init(self):
        tv = Television()
        assert tv._Television__status == False
        assert tv._Television__muted == False
        assert tv._Television__volume == Television.MIN_VOLUME
        assert tv._Television__channel == Television.MIN_CHANNEL

    def test_power(self):
        tv = Television()
        assert tv._Television__status == False
        tv.power()
        assert tv._Television__status == True
        tv.power()
        assert tv._Television__status == False


    def test_mute(self):
        tv = Television()
        tv.power()
        assert tv._Television__muted == False
        tv.mute()
        assert tv._Television__muted == True


    def test_channel_up(self):
        tv = Television()
        tv.power()
        tv._Television__channel = Television.MAX_CHANNEL
        tv.channel_up()
        assert tv._Television__channel == Television.MIN_CHANNEL
        tv._Television__channel = Television.MIN_CHANNEL
        tv.channel_up()
        assert tv._Television__channel == Television.MIN_CHANNEL + 1

    def test_channel_down(self):
        tv = Television()
        tv.power()
        tv.channel_down()
        assert tv._Television__channel == Television.MAX_CHANNEL
        tv._Television__channel = Television.MAX_CHANNEL
        tv.channel_down()
        assert tv._Television__channel == Television.MAX_CHANNEL - 1

    def test_volume_up(self):
        tv = Television()
        tv.power()
        tv._Television__volume = Television.MAX_VOLUME
        tv.volume_up()
        assert tv._Television__volume == Television.MAX_VOLUME
        tv._Television__volume = Television.MIN_VOLUME
        tv.volume_up()
        assert tv._Television__volume == Television.MIN_VOLUME + 1

    def test_volume_down(self):
        tv = Television()
        tv.power()
        tv._Television__volume = Television.MIN_VOLUME
        tv.volume_down()
        assert tv._Television__volume == Television.MIN_VOLUME
        tv._Television__volume = Television.MAX_VOLUME
        tv.volume_down()
        assert tv._Television__volume == Television.MAX_VOLUME - 1