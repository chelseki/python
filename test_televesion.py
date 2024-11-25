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

    def test_mute(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        assert tv._Television__volume == Television.MIN_VOLUME + 1
        tv.mute()
        assert tv._Television__muted == True
        assert tv._Television__volume == Television.MIN_VOLUME

        tv.mute()
        assert tv._Television__muted == False
        assert tv._Television__volume == Television.MIN_VOLUME + 1

        tv.mute()
        tv.power()
        assert tv._Television__muted == True
        assert tv._Television__status == False

        tv.power()
        assert tv._Television__muted == True
        tv.mute()
        assert tv._Television__muted == False
        assert tv._Television__volume == Television.MIN_VOLUME + 1


    def test_channel_up(self):
        tv = Television()
        tv.power()
        set_channel = tv._Television__channel
        tv.channel_up()
        if set_channel == Television.MAX_CHANNEL:
            assert tv._Television__channel == Television.MIN_CHANNEL
        else:
            assert tv._Television__channel == set_channel + 1

        set_channel = tv._Television__channel
        tv.channel_up()
        if set_channel == Television.MAX_CHANNEL:
            assert tv._Television__channel == Television.MIN_CHANNEL
        else:
            assert tv._Television__channel == set_channel + 1

        tv._Television__channel = Television.MAX_CHANNEL
        tv.channel_up()
        assert tv._Television__channel == Television.MIN_CHANNEL

    def test_channel_down(self):
        tv = Television()
        tv.power()
        set_channel = tv._Television__channel
        tv.channel_down()
        if set_channel == Television.MIN_CHANNEL:
            assert tv._Television__channel == Television.MAX_CHANNEL
        else:
            assert tv._Television__channel == set_channel - 1

        tv._Television__channel = Television.MIN_CHANNEL
        tv.channel_down()
        assert tv._Television__channel == Television.MAX_CHANNEL

    def test_volume_up(self):
        tv = Television()
        tv.volume_down()
        set_volume = tv._Television__volume
        assert tv._Television__volume == set_volume

        tv.power()
        tv.volume_up()
        assert tv._Television__volume == set_volume + 1

        tv.mute()
        assert tv._Television__muted == True
        tv.volume_up()
        assert tv._Television__muted == False
        assert tv._Television__volume == set_volume + 2

        tv._Television__volume = Television.MAX_VOLUME
        tv.volume_up()
        assert tv._Television__volume == Television.MAX_VOLUME

    def test_volume_down(self):
        tv = Television()
        tv.volume_down()
        set_volume = tv._Television__volume
        assert tv._Television__volume == set_volume

        tv.power()
        tv._Television__volume = Television.MAX_VOLUME
        set_volume = tv._Television__volume
        tv.volume_down()
        assert tv._Television__volume == set_volume - 1

        tv.mute()
        assert tv._Television__muted == True
        tv.volume_down()
        assert tv._Television__muted == False
        assert tv._Television__volume == tv._Television__prev_volume - 1