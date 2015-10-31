__author__ = 'adean'

from enums import event_type
from enums import trigger_rule

class MotionEvent(object):
    def __init__(self, media_file, event_type, event_time, event_id, file_type):
        self.media_file = media_file
        self.event_time = event_time
        self.event_id = event_id
        self.file_type = file_type
        self.event_type = event_type

    def get_event_actions_for_event(self, config):
        if self.event_type == event_type.EventType.on_event_start:
            return config.on_event_start_event_action_list;
        elif self.event_type == event_type.EventType.on_picture_save:
            return config.on_picture_save_event_action_list;
        elif self.event_type == event_type.EventType.on_movie_end:
            return config.on_movie_end_event_action_list;

    def get_actions_for_event(self, config, is_system_active):
        list_of_event_actions = self.get_event_actions_for_event(config);
        actions_to_perform = []
        for event_action in list_of_event_actions:
            if event_action.trigger_rule == trigger_rule.TriggerRule.always or (
                            event_action.trigger_rule == trigger_rule.TriggerRule.if_active and is_system_active):
                actions_to_perform.append(event_action.action_name)
        return actions_to_perform
