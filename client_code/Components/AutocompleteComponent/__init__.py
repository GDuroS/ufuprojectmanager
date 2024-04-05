from ._anvil_designer import AutocompleteComponentTemplate
from anvil import *
from anvil import server
import anvil.tables.query as q

from anvil.designer import in_designer

#from anvil_extras import non_blocking
from anvil_extras.animation import animate, Transition
from anvil_extras import augment

from OruData.Utils import ObjectUtils

from OruData.Utils.ValidationUtils import CustomValidationComponent

rotate_quad = Transition(rotate=[0, "90deg"])

class AutocompleteComponent(CustomValidationComponent, AutocompleteComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self._create_icon = 'fa:plus'
    self._continue_icon = 'fa:right-long'
    self._selected_value = None
    self._in = False
    self._entity_class = None
    
    super().__init__(comp_value_lambda=lambda x: self._selected_value)
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.role = 'autocomplete-component'
    self.create_or_next_button.role = [self.create_or_next_button.role, 'squared-button', 'autocomplete-input']
    self.clear_button.role = [self.clear_button.role, 'squared-button', 'clear-button', 'autocomplete-input']
    self.input_panel.role = 'autocomplete-input'
    self.input_box.role = 'autocomplete-input'
    self.result_grid.role = 'autocomplete-result'
    self.spinner_image.width = 41
    self.spinner_image.height = 41
    
    # Attributes for the search
    self._options = []
    self.result_grid_data.add_event_handler('x-item-selected', self.set_selected_value)
    if not in_designer:
      augment.set_event_handler(self, 'hover', self.focus_change)

  @property
  def result_attributes(self):
    return self.result_grid.columns

  @result_attributes.setter
  def result_attributes(self, attributes):
    self.result_grid.columns = attributes

  def create_or_next_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self._selected_value and self.show_continue_button:
      self.raise_event('continue_button_clicked', selected_value=self._selected_value)
    elif not self._selected_value and self.show_create_button:
      self.raise_event('new_button_clicked', text=self.input_box.text)

  def search(self, **event_args):
    """Runs the search using the parameters and text in the input_box"""
    query_value = self.input_box.text
    if len(query_value) >= self.min_length or query_value.endswith(" "):
      query_value = q.ilike('%' + query_value + '%')
      
      self.spinner_image.visible = True
      if self.filter_method:
        params = {}
        if self.filter_object:
          params = self.filter_object
        params[self.main_attribute] = query_value
        if self.use_entity_class:
          if self._entity_class is None:
            self._entity_class = self.use_entity_class
            if self._entity_class == 'default':
              from OruData.Model.Entity import Entity
              self._entity_class = Entity
          self._options = ObjectUtils.search_iterator_to_entity_class_list(server.call_s(self.filter_method, **params), self._entity_class)
        else:
          self._options = server.call_s(self.filter_method, **params)
      else:
        raise ValueError('filter method not provided')
      
      self.spinner_image.visible = False
      self.result_grid_data.items = self._options
    elif query_value == '':
      self.result_grid_data.items = []

  def input_box_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self._selected_value:
      self._selected_value = None
      self.refresh_data_bindings()
    self.search(**event_args)

  def set_selected_value(self, value, **event_args):
    self._selected_value = value
    self.input_box.text = value[self.main_attribute] if value is not None else None
    self.result_grid_data.items = []
    self._update_action_button_status()
    self.refresh_data_bindings()
    self.raise_event('selected_value_change', selected_value=self._selected_value)

  def _update_action_button_status(self, **event_args):
    curr_status = self.create_or_next_button.icon
    new_status = curr_status
    if self._selected_value:
      self.create_or_next_button.visible = self.show_continue_button
      new_status = self._continue_icon
    else:
      self.create_or_next_button.visible = self.show_create_button
      new_status = self._create_icon
    if curr_status != new_status:
      animate(self.create_or_next_button, rotate_quad, duration=25).wait()
      self.create_or_next_button.icon = new_status

  def clear_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.set_selected_value(None)
    self.refresh_data_bindings()

  def focus_change(self, **event_args):
    """This method is called when the TextBox gets focus"""
    if event_args.get('event_type'):
      self._in = event_args.get('event_type') == 'mouseenter'
    if event_args.get('event_name') == 'focus':
      self.result_grid.visible = True
    elif get_focused_component() is not self.input_box and not self._in:
      self.result_grid.visible = False



      
    
