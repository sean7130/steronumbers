### GLOBAL VARIABLES BY DESIGN ###
start_color = (149, 114, 255)
end_color = (0, 170, 255)

text_color = None
user_gradient = ""
style_sheet = ""

def add_tint(color, tint_factor):
    """
    standard procedure to add tint
    """
    if not (0 <= tint_factor <= 1):
        raise ValueError("Tint factor must be between 0 and 1")

    r, g, b = color
    r_tinted = int(r + (255 - r) * tint_factor)
    g_tinted = int(g + (255 - g) * tint_factor)
    b_tinted = int(b + (255 - b) * tint_factor)

    return (r_tinted, g_tinted, b_tinted)


def decrease_saturation(color, saturation_factor):
    """
    Decrease the saturation of an RGB color.
    :param color: A tuple of integers (r, g, b), each ranging from 0 to 255.
    :param saturation_factor: A float between 0 and 1, where 0 is fully grayscale.
    :return: A tuple of integers (r, g, b) representing the desaturated color.
    """
    # Ensure the saturation factor is within bounds
    if not (0 <= saturation_factor <= 1):
        raise ValueError("Saturation factor must be between 0 and 1")

    r, g, b = color
    # Calculate the grayscale value (luminance)
    gray = int(0.299 * r + 0.587 * g + 0.114 * b)  # Standard luminance formula

    r_desaturated = int(r * saturation_factor + gray * (1 - saturation_factor))
    g_desaturated = int(g * saturation_factor + gray * (1 - saturation_factor))
    b_desaturated = int(b * saturation_factor + gray * (1 - saturation_factor))

    return (r_desaturated, g_desaturated, b_desaturated)


def gen_text_color(base_color, delta=-40):
  ret = [e+delta for e in base_color]
  for i in range(len(ret)):
    if ret[i] < 0:
      ret[i] = 0
    if ret[i] > 230:
      ret[i] = 230 
  return tuple(ret)


def update_color_schemes(s_color, t_color, tmp_stylesheet=False):
  # tmp_stylesheet means the generated stylesheet will not be used globally
  if not tmp_stylesheet:
    global stylesheet

  global user_gradient
  global start_color
  global end_color
  global text_color

  start_color = f"rgb{s_color}"
  end_color = f"rgb{t_color}"
  text_color = f"rgb{gen_text_color(t_color)}"
  light_accent = f"rgb{gen_text_color(t_color, 120)}"
  button_color = f"rgb{decrease_saturation(add_tint(t_color, 0.85), 0.45)}"
  button_after_pressed = f"rgb{decrease_saturation(add_tint(t_color, 0.90), 0.45)}"

  standard_bottom_boarder_color = "#e5e5e5"
  # standard_bottom_boarder_color = "#e0e0e0" #experimental 

  user_gradient = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 %s, stop:1 %s)" % (start_color, end_color)
  stylesheet = '''

  *{
    color: #555555;

    font-family: Roboto;


      font-size: 13.0px;



      line-height: 4px;


    selection-background-color: %s;
    selection-color: #3c3c3c;
  }

  *:focus {
     outline: none;
  }

  /*  ------------------------------------------------------------------------  */
  /*  Custom colors  */

  .danger{
    color: #dc3545;
    background-color: transparent;
  }

  .warning{
    color: #ffc107;
    background-color: transparent;
  }

  .success{
    color: #17a2b8;
    background-color: transparent;
  }

  .danger:disabled{
    color: rgba(220, 53, 69, 0.4);
    border-color: rgba(220, 53, 69, 0.4);
  }

  .warning:disabled{
    color: rgba(255, 193, 7, 0.4);
    border-color: rgba(255, 193, 7, 0.4);
  }

  .success:disabled{
    color: rgba(23, 162, 184, 0.4);
    border-color: rgba(23, 162, 184, 0.4);
  }

  .danger:flat:disabled{
    background-color: rgba(220, 53, 69, 0.1);
  }

  .warning:flat:disabled{
    background-color: rgba(255, 193, 7, 0.1);
  }

  .success:flat:disabled{
    background-color: rgba(23, 162, 184, 0.1);
  }

  /*  ------------------------------------------------------------------------  */
  /*  Basic widgets  */

  QWidget {
    background-color: #fbfbfb;
  }

  QGroupBox {
    background-color: #fbfbfb;
    border: 1px solid #f0f0f9;
    border-bottom: 3px solid %s;
    border-radius: 4px;
  }

  QFrame {
    background: transparent;
  }

  QGroupBox.fill_background {
    background-color: #f5f5f5;
    border: 2px solid #f5f5f5;
    border-radius: 4px;
  }

  QSplitter {
    background-color: transparent;
    border: none
  }

  QStatusBar {
    color: #555555;
    background-color: rgba(230, 230, 230, 0.2);
    border-radius: 0px;
  }

  QScrollArea,
  QStackedWidget,
  QWidget > QToolBox,
  QToolBox > QWidget,
  QTabWidget > QWidget {
    border: none;
  }

  QTabWidget::pane {
    border: none;
  }

  /*  ------------------------------------------------------------------------  */
  /*  Inputs  */

  QDateEdit,
  QDateTimeEdit,
  QSpinBox,
  QDoubleSpinBox,
  QTextEdit,
  QLineEdit,
  QPushButton {
    color: %s;
    background-color: #ffffff;
    border: 2px solid %s;
    border-radius: 4px;
    height: 32px;
  }

  QDateEdit,
  QDateTimeEdit,
  QSpinBox,
  QDoubleSpinBox,
  QTreeView,
  QListView,
  QLineEdit,
  QComboBox {
    color: #3c3c3c;
    padding-left: 16px;
    border-radius: 0px;
    border-radius: 0px;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    height: 32px;
    background-color: rgba(245, 245, 245, 0.75);
    border: 2px solid %s;
    border-width: 0 0 2px 0;
  }


  QDateEdit:hover,
  QDateTimeEdit:hover,
  QSpinBox:hover,
  QDoubleSpinBox:hover,
  QTreeView:hover,
  QListView:hover,
  QLineEdit:hover,
  QComboBox:hover {
    color: #3c3c3c;
    padding-left: 16px;
    border-radius: 0px;
    border-radius: 0px;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    height: 32px;
    background-color: rgba(245, 245, 245, 0.75);
    border: 2px solid %s;
    border-width: 0 0 2px 0;
  }

  QPlainTextEdit {
    border-radius: 4px;
    padding: 8px 16px;
    background-color: #ffffff;
    border: 2px solid #e6e6e6;
  }

  QTextEdit {
    padding: 8px 16px;
    border-radius: 4px;
    background-color: #f5f5f5;
  }

  QDateEdit:disabled,
  QDateTimeEdit:disabled,
  QSpinBox:disabled,
  QDoubleSpinBox:disabled,
  QTextEdit:disabled,
  QLineEdit:disabled {
    color: rgba(85, 85, 85, 0.2);
    background-color: rgba(245, 245, 245, 0.3);
    border: 2px solid #f5f5f5;
    border-width: 0 0 2px 0;
    padding: 0px 16px;
    border-radius: 0px;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    height: 32px;
  }

  /*  ------------------------------------------------------------------------  */
  /*  QComboBox  */

  QDateEdit,
  QComboBox {
    color: #3c3c3c;
    border: 2px solid %s;
    border-radius: 0px;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    height: 32px;
    background-color: rgba(245, 245, 245, 0.75);
    border: 2px solid rgba(85, 85, 85, 0.2);
    border-width: 0 0 2px 0;
  }

  QDateEdit:disabled,
  QComboBox:disabled {
    color: rgba(85, 85, 85, 0.2);
    background-color: rgba(245, 245, 245, 0.3);
    border-bottom: 2px solid #f5f5f5;
  }

  QDateEdit::drop-down,
  QComboBox::drop-down {
    border: none;
    color: %s;
    width: 20px;
  }

  QDateEdit::down-arrow,
  QComboBox::down-arrow {
    image: url(icon:/active/downarrow.svg);
    margin-right: 12px;
  }


  QDateEdit::down-arrow:focus,
  QComboBox::down-arrow:focus {
    image: url(icon:/primary/downarrow.svg);
    margin-right: 12px;
  }

  QDateEdit::down-arrow:disabled,
  QComboBox::down-arrow:disabled {
    image: url(icon:/disabled/downarrow.svg);
    margin-right: 12px;
  }

  QDateEdit QAbstractItemView,
  QComboBox QAbstractItemView {
    background-color: #f5f5f5;
    border: 2px solid #e6e6e6;
    border-radius: 4px;
  }

  QDateEdit[frame='false'],
  QComboBox[frame='false'] {
    color: #555555;
    background-color: transparent;
    border: 1px solid transparent;
  }

  QDateEdit[frame='false']:disabled,
  QComboBox[frame='false']:disabled {
    color: rgba(85, 85, 85, 0.2);
  }

  /*  ------------------------------------------------------------------------  */
  /*  Spin buttons  */

  QDateTimeEdit::up-button,
  QDoubleSpinBox::up-button,
  QSpinBox::up-button {
    subcontrol-origin: border;
    subcontrol-position: top right;
    width: 20px;
    image: url(icon:/active/uparrow.svg);
    border-width: 0px;
    margin-right: 5px;
  }

  QDateTimeEdit::up-button:disabled,
  QDoubleSpinBox::up-button:disabled,
  QSpinBox::up-button:disabled {
    image: url(icon:/disabled/uparrow.svg);
  }

  QDateTimeEdit::down-button,
  QDoubleSpinBox::down-button,
  QSpinBox::down-button {
    subcontrol-origin: border;
    subcontrol-position: bottom right;
    width: 20px;
    image: url(icon:/active/downarrow.svg);
    border-width: 0px;
    border-top-width: 0;
    margin-right: 5px;
  }

  QDateTimeEdit::down-button:disabled,
  QDoubleSpinBox::down-button:disabled,
  QSpinBox::down-button:disabled {
    image: url(icon:/disabled/downarrow.svg);
  }

  QDoubleSpinBox#width_adjust_spinbox,
  QDoubleSpinBox#height_adjust_spinbox {
    background-color: #ffffff;
    border-radius: 4px;
    height: 32px;
  }

  QDoubleSpinBox#width_adjust_spinbox:hover,
  QDoubleSpinBox#height_adjust_spinbox:hover {
    background-color: #ffffff;
    border-radius: 4px;
    height: 32px;
    border: 2px solid %s;
    border-width: 0 0 2px 0;
  }

  /*  ------------------------------------------------------------------------  */
  /*  QPushButton  */

  QPushButton {
    text-transform: uppercase;
    margin: 0px;
    padding: 1px 16px;
    height: 32px;
    font-weight: bold;


      border-radius: 4px;

  }

  QPushButton:checked,
  QPushButton:pressed {
    color: #ffffff;
    background-color: #2979ff;
  }

  QPushButton:flat {
    margin: 0px;
    color: %s;
    border: none;
    background-color: transparent;
  }

  QPushButton:flat:hover {
    background-color: %s;
  }

  QPushButton:flat:pressed,
  QPushButton:flat:checked {
    background-color: rgba(41, 121, 255, 0.1);
  }

  QPushButton:disabled {
    color: rgba(230, 230, 230, 0.75);
    background-color: transparent;
    border-color:  #e6e6e6;
  }

  QPushButton:flat:disabled {
    color: rgba(230, 230, 230, 0.75);
    background-color: rgba(230, 230, 230, 0.25);
    border: none;
  }

  QPushButton:disabled {
    border: 2px solid rgba(230, 230, 230, 0.75);
  }

  QPushButton:checked:disabled {
    color: #f5f5f5;
    background-color: #e6e6e6;
    border-color:  #e6e6e6;
  }

  QToolButton:focus,
  QPushButton:focus {
    background-color: %s;
  }

  QPushButton:checked:focus,
  QPushButton:pressed:focus {
    background-color: %s;
  }

  QPushButton:flat:focus {
    border: none;
    background-color: %s;
  }

  QPushButton:hover  {
    background-color: %s
  }


  /*  ------------------------------------------------------------------------  */
  /*  QTabBar  */

  QTabBar{
    text-transform: uppercase;
    font-weight: bold;
  }

  QTabBar::tab {
    color: #555555;
    border: 0px;
  }

  QTabBar::tab:bottom,
  QTabBar::tab:top{
    padding: 0 16px;
    height: 28px;
  }

  QTabBar::tab:left,
  QTabBar::tab:right{
    padding: 16px 0;
    width: 28px;
  }

  QTabBar::tab:top:selected,
  QTabBar::tab:top:hover {
    color: #2979ff;
    border-bottom: 2px solid #2979ff;
  }

  QTabBar::tab:bottom:selected,
  QTabBar::tab:bottom:hover {
    color: #2979ff;
    border-top: 2px solid #2979ff;
  }

  QTabBar::tab:right:selected,
  QTabBar::tab:right:hover {
    color: #2979ff;
    border-left: 2px solid #2979ff;
  }

  QTabBar::tab:left:selected,
  QTabBar::tab:left:hover {
    color: #2979ff;
    border-right: 2px solid #2979ff;
  }

  QTabBar QToolButton:hover,
  QTabBar QToolButton {
    border: 0px;
    background-color: #f5f5f5;
    background: #f5f5f5;
  }

  QTabBar QToolButton::up-arrow {
    image: url(icon:/primary/uparrow2.svg);
    width: 28px;
  }

  QTabBar QToolButton::down-arrow {
    image: url(icon:/primary/downarrow2.svg);
    width: 28px;
  }

  QTabBar QToolButton::right-arrow {
    image: url(icon:/disabled/rightarrow2.svg);
    height: 28px;
  }

  QTabBar QToolButton::left-arrow {
    image: url(icon:/disabled/leftarrow2.svg);
    height: 28px;
  }

  QTabBar::close-button {
    image: url(icon:/primary/tab_close.svg);
  }

  QTabBar::close-button:hover {
    image: url(icon:/primary/tab_close.svg);
  }

  /*  ------------------------------------------------------------------------  */
  /*  QGroupBox  */

  QGroupBox {
    padding: 16px;
    padding-top: 36px;
    line-height: 13px;
    text-transform: uppercase;
    font-size: 13px;
    font-weight: bold;
  }

  QGroupBox::title {
    color: rgba(85, 85, 85, 0.4);
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 16px;
    background-color: #ffffff;
    background-color: transparent;
    height: 36px;
  }

  /*  ------------------------------------------------------------------------  */
  /*  QRadioButton and QCheckBox labels  */

  QRadioButton,
  QCheckBox {
    spacing: 12px;
    color: #555555;
    line-height: 14px;
    height: 36px;
    background-color: transparent;
    spacing: 5px;
  }

  QRadioButton:disabled,
  QCheckBox:disabled {
    color: rgba(85, 85, 85, 0.3);
  }

  /*  ------------------------------------------------------------------------  */
  /*  General Indicators  */

  QGroupBox::indicator {
    width: 24px;
    height: 24px;
    border-radius: 3px;
  }

  QMenu::indicator,
  QListView::indicator,
  QTableWidget::indicator,
  QRadioButton::indicator,
  QCheckBox::indicator {
    width: 28px;
    height: 28px;
    border-radius: 4px;
   }

  /*  ------------------------------------------------------------------------  */
  /*  QListView Indicator  */

  QListView::indicator:checked,
  QListView::indicator:checked:selected,
  QListView::indicator:checked:focus {
    image: url(icon:/primary/checklist.svg);
  }

  QListView::indicator:checked:selected:active {
    image: url(icon:/primary/checklist_invert.svg);
  }

  QListView::indicator:checked:disabled {
    image: url(icon:/disabled/checklist.svg);
  }

  QListView::indicator:indeterminate,
  QListView::indicator:indeterminate:selected,
  QListView::indicator:indeterminate:focus {
    image: url(icon:/primary/checklist_indeterminate.svg);
  }

  QListView::indicator:indeterminate:selected:active {
    image: url(icon:/primary/checklist_indeterminate_invert.svg);
  }

  QListView::indicator:indeterminate:disabled {
    image: url(icon:/disabled/checklist_indeterminate.svg);
  }

  /*  ------------------------------------------------------------------------  */
  /*  QTableView Indicator  */

  QTableView::indicator:enabled:checked,
  QTableView::indicator:enabled:checked:selected,
  QTableView::indicator:enabled:checked:focus {
    image: url(icon:/primary/checkbox_checked.svg);
  }

  QTableView::indicator:checked:selected:active {
    image: url(icon:/primary/checkbox_checked_invert.svg);
  }

  QTableView::indicator:disabled:checked,
  QTableView::indicator:disabled:checked:selected,
  QTableView::indicator:disabled:checked:focus {
    image: url(icon:/disabled/checkbox_checked.svg);
  }

  QTableView::indicator:enabled:unchecked,
  QTableView::indicator:enabled:unchecked:selected,
  QTableView::indicator:enabled:unchecked:focus {
    image: url(icon:/primary/checkbox_unchecked.svg);
  }

  QTableView::indicator:unchecked:selected:active {
    image: url(icon:/primary/checkbox_unchecked_invert.svg);
  }

  QTableView::indicator:disabled:unchecked,
  QTableView::indicator:disabled:unchecked:selected,
  QTableView::indicator:disabled:unchecked:focus {
    image: url(icon:/disabled/checkbox_unchecked.svg);
  }

  QTableView::indicator:enabled:indeterminate,
  QTableView::indicator:enabled:indeterminate:selected,
  QTableView::indicator:enabled:indeterminate:focus {
    image: url(icon:/primary/checkbox_indeterminate.svg);
  }

  QTableView::indicator:indeterminate:selected:active {
    image: url(icon:/primary/checkbox_indeterminate_invert.svg);
  }

  QTableView::indicator:disabled:indeterminate,
  QTableView::indicator:disabled:indeterminate:selected,
  QTableView::indicator:disabled:indeterminate:focus {
    image: url(icon:/disabled/checkbox_indeterminate.svg);
  }

  /*  ------------------------------------------------------------------------  */
  /*  QCheckBox and QGroupBox Indicator  */

  QCheckBox::indicator:checked,
  QGroupBox::indicator:checked {
    image: url(icon:/primary/checkbox_checked.svg);
  }

  QCheckBox::indicator:unchecked,
  QGroupBox::indicator:unchecked {
    image: url(icon:/primary/checkbox_unchecked.svg);
  }

  QCheckBox::indicator:indeterminate,
  QGroupBox::indicator:indeterminate {
    image: url(icon:/primary/checkbox_indeterminate.svg);
  }

  QCheckBox::indicator:checked:disabled,
  QGroupBox::indicator:checked:disabled {
    image: url(icon:/disabled/checkbox_checked.svg);
  }

  QCheckBox::indicator:unchecked:disabled,
  QGroupBox::indicator:unchecked:disabled {
    image: url(icon:/disabled/checkbox_unchecked.svg);
  }

  QCheckBox::indicator:indeterminate:disabled,
  QGroupBox::indicator:indeterminate:disabled {
    image: url(icon:/disabled/checkbox_indeterminate.svg);
  }

  /*  ------------------------------------------------------------------------  */
  /*  QRadioButton Indicator  */

  QRadioButton::indicator:checked {
    image: url(icon:/primary/radiobutton_checked.svg);
  }

  QRadioButton::indicator:unchecked {
    image: url(icon:/primary/radiobutton_unchecked.svg);
  }

  QRadioButton::indicator:checked:disabled {
    image: url(icon:/disabled/radiobutton_checked.svg);
  }

  QRadioButton::indicator:unchecked:disabled {
    image: url(icon:/disabled/radiobutton_unchecked.svg);
  }


  /*  ------------------------------------------------------------------------  */
  /*  QDockWidget  */

  QDockWidget {
    color: #555555;
    text-transform: uppercase;
    border: 2px solid #f5f5f5;
    titlebar-close-icon: url(icon:/primary/close.svg);
    titlebar-normal-icon: url(icon:/primary/float.svg);
    border-radius: 4px;
  }

  QDockWidget::title {
    text-align: left;
    padding-left: 36px;
    padding: 3px;
    margin-top: 4px;
  }

  /*  ------------------------------------------------------------------------  */
  /*  QComboBox indicator  */

  QComboBox::indicator:checked {
    image: url(icon:/primary/checklist.svg);
  }

  QComboBox::indicator:checked:selected {
    image: url(icon:/primary/checklist_invert.svg);
  }

  /*  ------------------------------------------------------------------------  */
  /*  Menu Items  */

  QComboBox::item,
  QCalendarWidget QMenu::item,
  QMenu::item {

      height: 28px;

    border: 8px solid transparent;
    color: #555555;
  }

  QCalendarWidget QMenu::item,
  QMenu::item {


        padding: 0px 24px 0px 8px;  /* pyqt5 */


  }


  QComboBox::item:selected,
  QCalendarWidget QMenu::item:selected,
  QMenu::item:selected {
    color: #3c3c3c;
    background-color: %s;
    border-radius: 0px;
  }

  QComboBox::item:disabled,
  QCalendarWidget QMenu::item:disabled,
  QMenu::item:disabled {
    color: rgba(85, 85, 85, 0.3);
  }

  /*  ------------------------------------------------------------------------  */
  /*  QMenu  */

  QCalendarWidget QMenu,
  QMenu {
    background-color: #f5f5f5;
    border: 2px solid #e6e6e6;
    border-radius: 4px;
  }

  QMenu::separator {
    height: 2px;
    background-color: #e6e6e6;
    margin-left: 2px;
    margin-right: 2px;
  }

  QMenu::right-arrow{
    image: url(icon:/primary/rightarrow.svg);
    width: 16px;
    height: 16px;
  }

  QMenu::right-arrow:selected{
    image: url(icon:/disabled/rightarrow.svg);
  }

  QMenu::indicator:non-exclusive:unchecked {
    image: url(icon:/primary/checkbox_unchecked.svg);
  }

  QMenu::indicator:non-exclusive:unchecked:selected {
    image: url(icon:/primary/checkbox_unchecked_invert.svg);
  }

  QMenu::indicator:non-exclusive:checked {
    image: url(icon:/primary/checkbox_checked.svg);
  }

  QMenu::indicator:non-exclusive:checked:selected {
    image: url(icon:/primary/checkbox_checked_invert.svg);
  }

  QMenu::indicator:exclusive:unchecked {
    image: url(icon:/primary/radiobutton_unchecked.svg);
  }

  QMenu::indicator:exclusive:unchecked:selected {
    image: url(icon:/primary/radiobutton_unchecked_invert.svg);
  }

  QMenu::indicator:exclusive:checked {
    image: url(icon:/primary/radiobutton_checked.svg);
  }

  QMenu::indicator:exclusive:checked:selected {
    image: url(icon:/primary/radiobutton_checked_invert.svg);
  }

  /*  ------------------------------------------------------------------------  */
  /*  QMenuBar  */

  QMenuBar {
    background-color: #ffffff;
    color: #555555;
  }

  QMenuBar::item {
    height: 32px;
    padding: 8px;
    background-color: transparent;
    color: #555555;
  }

  QMenuBar::item:selected,
  QMenuBar::item:pressed {
    color: #3c3c3c;
    background-color: %s;
  }

  /*  ------------------------------------------------------------------------  */
  /*  QToolBox  */

  QToolBox::tab {
    background-color: #f5f5f5;
    color: #555555;
    text-transform: uppercase;
    border-radius: 4px;
    padding-left: 15px;
  }

  QToolBox::tab:selected,
  QToolBox::tab:hover {
    background-color: rgba(41, 121, 255, 0.2);
  }

  /*  ------------------------------------------------------------------------  */
  /*  QProgressBar  */

  QProgressBar {
    border-radius: 0;
    background-color: #e6e6e6;
    text-align: center;
    color: transparent;
  }

  QProgressBar::chunk {
    background-color: #2979ff;
  }

  /*  ------------------------------------------------------------------------  */
  /*  QScrollBar  */

  QScrollBar:horizontal {
    border: 0;
    background: #f5f5f5;
    height: 8px;
  }

  QScrollBar:vertical {
    border: 0;
    background: #f5f5f5;
    width: 8px;
  }

  QScrollBar::handle {
    background: %s;
  }

  QScrollBar::handle:horizontal {
    min-width: 24px;
  }

  QScrollBar::handle:vertical {
    min-height: 24px;
  }

  QScrollBar::handle:vertical:hover,
  QScrollBar::handle:horizontal:hover {
    background: %s;
  }

  QScrollBar::add-line:vertical,
  QScrollBar::sub-line:vertical,
  QScrollBar::add-line:horizontal,
  QScrollBar::sub-line:horizontal {
    border: 0;
    background: transparent;
    width: 0px;
    height: 0px;
  }

  QScrollBar::sub-page:horizontal,
  QScrollBar::add-page:horizontal,
  QScrollBar::sub-page:vertical,
  QScrollBar::add-page:vertical,
  QScrolLBar:vertical {
      background: transparent;
  }

  /*  ------------------------------------------------------------------------  */
  /*  QScrollBar-Big  */

  QScrollBar.big:horizontal {
    border: 0;
    background: #f5f5f5;
    height: 36px;
  }

  QScrollBar.big:vertical {
    border: 0;
    background: #f5f5f5;
    width: 36px;
  }

  QScrollBar.big::handle,
  QScrollBar.big::handle:vertical:hover,
  QScrollBar.big::handle:horizontal:hover {
    background: #2979ff;
  }

  QScrollBar.big::handle:horizontal {
    min-width: 24px;
  }

  QScrollBar.big::handle:vertical {
    min-height: 24px;
  }

  QScrollBar.big::add-line:vertical,
  QScrollBar.big::sub-line:vertical,
  QScrollBar.big::add-line:horizontal,
  QScrollBar.big::sub-line:horizontal {
    border: 0;
    background: transparent;
    width: 0px;
    height: 0px;
  }

  /*  ------------------------------------------------------------------------  */
  /*  QSlider  */

  QSlider:horizontal {
    min-height: 24px;
    max-height: 24px;
  }

  QSlider:vertical {
    min-width: 24px;
    max-width: 24px;
  }

  QSlider::groove:horizontal {
    height: 4px;
    background: #393939;
    margin: 0 12px;
  }

  QSlider::groove:vertical {
    width: 4px;
    background: #393939;
    margin: 12px 0;
  }

  QSlider::handle:horizontal {
    image: url(icon:/primary/slider.svg);
    width: 18px;
    height: 18px;
    margin: -18px -9px;
  }

  QSlider::handle:vertical {
    image: url(icon:/primary/slider.svg);
    width: 18px;
    height: 18px;
    margin: -9px -18px;
  }

  QSlider::add-page {
  background: #f5f5f5;
  }

  QSlider::sub-page {
  background: %s;
  }

  /*  ------------------------------------------------------------------------  */
  /*  QLabel  */

  QLabel {
    border: none;
    background: transparent;
    color: #555555
  }

  QLabel:disabled {
    color: rgba(85, 85, 85, 0.2)
  }

  /*  ------------------------------------------------------------------------  */
  /*  VLines and HLinex  */

  QFrame[frameShape="4"] {
      border-width: 1px 0 0 0;
      background: none;
  }

  QFrame[frameShape="5"] {
      border-width: 0 1px 0 0;
      background: none;
  }

  QFrame[frameShape="4"],
  QFrame[frameShape="5"] {
    border-color: #fbfbfb; /* edit */
  }

  /*  ------------------------------------------------------------------------  */
  /*  QToolBar  */

  QToolBar {
    background: #ffffff;
    border: 0px solid;
  }

  QToolBar:horizontal {
    border-bottom: 1px solid #e6e6e6;
  }

  QToolBar:vertical {
    border-right: 1px solid #e6e6e6;
  }

  QToolBar::handle:horizontal {
    image: url(icon:/primary/toolbar-handle-horizontal.svg);
  }

  QToolBar::handle:vertical {
    image: url(icon:/primary/toolbar-handle-vertical.svg);
  }

  QToolBar::separator:horizontal {
    border-right: 1px solid #e6e6e6;
    border-left: 1px solid #e6e6e6;
    width: 1px;
  }

  QToolBar::separator:vertical {
    border-top: 1px solid #e6e6e6;
    border-bottom: 1px solid #e6e6e6;
    height: 1px;
  }


  /*  ------------------------------------------------------------------------  */
  /*  QToolButton  */

  QToolButton {
    background: #ffffff;
    border: 0px;
    height: 36px;
    margin: 3px;
    padding: 3px;
    border-right: 12px solid #ffffff;
    border-left: 12px solid #ffffff;
  }

  QToolButton:hover {
    background: #e6e6e6;
    border-right: 12px solid #e6e6e6;
    border-left: 12px solid #e6e6e6;
  }

  QToolButton:pressed {
    background: #f5f5f5;
    border-right: 12px solid #f5f5f5;
    border-left: 12px solid #f5f5f5;
  }

  QToolButton:checked {
    background: #e6e6e6;
    border-left: 12px solid #e6e6e6;
    border-right: 12px solid #2979ff;
  }

  /*  ------------------------------------------------------------------------  */
  /*  General viewers  */

  QTableView {
    background-color: #ffffff;
    border: 1px solid #f5f5f5;
    border-radius: 4px;
  }

  QTreeView,
  QListView {
    border-radius: 4px;
    padding: 4px;
    margin: 0px;
    border: 0px;
  }

  QTableView::item,
  QTreeView::item,
  QListView::item {
    padding: 4px;
    min-height: 32px;
    color: #555555;
    selection-color: #555555; /* For Windows */
    border-color: transparent;  /* Fix #34 */
  }

  /*  ------------------------------------------------------------------------  */
  /*  Items Selection */

  QTableView::item:selected,
  QTreeView::item:selected,
  QListView::item:selected {
    background-color: %s;
    selection-background-color: %s;
    color: #555555;
    selection-color: #555555; /* For Windows */
  }

  QTableView::item:selected:focus,
  QTreeView::item:selected:focus,
  QListView::item:selected:focus {
    background-color: %s;
    selection-background-color: %s;
    color: #3c3c3c;
    selection-color: #3c3c3c; /* For Windows */
  }

  QTableView {
    selection-background-color: rgba(41, 121, 255, 0.2);
  }

  QTableView:focus {
    selection-background-color: %s;
  }

  QTableView::item:disabled {
    color: rgba(85, 85, 85, 0.3);
    selection-color: rgba(85, 85, 85, 0.3);
    background-color: #f5f5f5;
    selection-background-color: #f5f5f5;
  }

  /*  ------------------------------------------------------------------------  */
  /*  QTreeView  */

  QTreeView::branch{
    background-color: #f5f5f5;
  }

  QTreeView::branch:closed:has-children:has-siblings,
  QTreeView::branch:closed:has-children:!has-siblings {
    image: url(icon:/primary/branch-closed.svg);
  }

  QTreeView::branch:open:has-children:!has-siblings,
  QTreeView::branch:open:has-children:has-siblings {
    image: url(icon:/primary/branch-open.svg);
  }

  QTreeView::branch:has-siblings:!adjoins-item {
    border-image: url(icon:/disabled/vline.svg) 0;
  }

  QTreeView::branch:has-siblings:adjoins-item {
      border-image: url(icon:/disabled/branch-more.svg) 0;
  }

  QTreeView::branch:!has-children:!has-siblings:adjoins-item,
  QTreeView::branch:has-children:!has-siblings:adjoins-item {
      border-image: url(icon:/disabled/branch-end.svg) 0;
  }

  QTreeView QHeaderView::section {
    border: none;
  }


  /*  ------------------------------------------------------------------------  */
  /*  Custom buttons  */

  QPushButton.danger {
    border-color: #dc3545;
    color: #dc3545;
  }

  QPushButton.danger:checked,
  QPushButton.danger:pressed {
    color: #ffffff;
    background-color: #dc3545;
  }

  QPushButton.warning{
    border-color: #ffc107;
    color: #ffc107;
  }

  QPushButton.warning:checked,
  QPushButton.warning:pressed {
    color: #ffffff;
    background-color: #ffc107;
  }

  QPushButton.success {
    border-color: #17a2b8;
    color: #17a2b8;
  }

  QPushButton.success:checked,
  QPushButton.success:pressed {
    color: #ffffff;
    background-color: #17a2b8;
  }

  QPushButton.danger:flat:hover {
    background-color: rgba(220, 53, 69, 0.2);
  }

  QPushButton.danger:flat:pressed,
  QPushButton.danger:flat:checked {
    background-color: rgba(220, 53, 69, 0.1);
    color: #dc3545;
  }

  QPushButton.warning:flat:hover {
    background-color: rgba(255, 193, 7, 0.2);
  }

  QPushButton.warning:flat:pressed,
  QPushButton.warning:flat:checked {
    background-color: rgba(255, 193, 7, 0.1);
    color: #ffc107;
  }

  QPushButton.success:flat:hover {
    background-color: rgba(23, 162, 184, 0.2);
  }

  QPushButton.success:flat:pressed,
  QPushButton.success:flat:checked {
    background-color: rgba(23, 162, 184, 0.1);
    color: #17a2b8;
  }

  /*  ------------------------------------------------------------------------  */
  /*  QTableView  */

  QTableCornerButton::section {
    background-color: #f5f5f5;
    border-radius: 0px;
    border-right: 1px solid;
    border-bottom: 1px solid;
    border-color: #ffffff;
  }

  QTableView {
    alternate-background-color: rgba(245, 245, 245, 0.7);
  }

  QHeaderView {
    border: none;
  }

  QHeaderView::section {
    color: rgba(85, 85, 85, 0.7);
    text-transform: uppercase;
    background-color: #f5f5f5;
    padding: 0 24px;
    height: 36px;
    border-radius: 0px;
    border-right: 1px solid;
    border-bottom: 1px solid;
    border-color: #ffffff;
  }

  QHeaderView::section:vertical {

  }

  QHeaderView::section:horizontal {

  }

  /*  ------------------------------------------------------------------------  */
  /*  QLCDNumber  */

  QLCDNumber {
    color: #2979ff;
    background-color:rgba(41, 121, 255, 0.1);
    border: 1px solid rgba(41, 121, 255, 0.3);
    border-radius: 4px;
  }

  /*  ------------------------------------------------------------------------  */
  /*  QCalendarWidget  */

  QCalendarWidget {
    min-height: 300px;
  }

#qt_calendar_prevmonth {
    qproperty-icon: url(icon:/primary/leftarrow.svg);
  }

#qt_calendar_nextmonth {
    qproperty-icon: url(icon:/primary/rightarrow.svg);
  }

  /*  ------------------------------------------------------------------------  */
  /*  Inline QLineEdit  */

  QTreeView QLineEdit,
  QTableView QLineEdit,
  QListView QLineEdit {
    color: #555555;
    background-color: #f5f5f5;
    border: 1px solid unset;
    border-radius: unset;
    padding: unset;
    padding-left: unset;
    height: unset;
    border-width: unset;
    border-top-left-radius: unset;
    border-top-right-radius: unset;
  }

  /*  ------------------------------------------------------------------------  */
  /*  QToolTip  */

  QToolTip {
    padding: 4px;
    border: 1px solid #ffffff;
    border-radius: 4px;
    color: #555555;
    background-color: #e6e6e6;
  }

  /*  ------------------------------------------------------------------------  */
  /*  QDialog  */



  QDialog QToolButton:disabled {
    background-color: #f5f5f5;
    color: #555555
  }

  /*  ------------------------------------------------------------------------  */

  QDateTimeEdit::down-button:focus,
  QDoubleSpinBox::down-button:focus,
  QSpinBox::down-button:focus {
    image: url(icon:/primary/downarrow.svg);
  }

  QMenu::indicator:focus,
  QListView::indicator:focus,
  QTableWidget::indicator:focus,
  QRadioButton::indicator:focus {
    background-color: rgba(41, 121, 255, 0.2);
    border-radius: 14px;
   }

  QCheckBox::indicator:focus {
    background-color: rgba(41, 121, 255, 0.2);
   }
  ''' % (light_accent,
         standard_bottom_boarder_color, #groupbox bottom border
         text_color,  #pushbutton text
         user_gradient, 
         standard_bottom_boarder_color, #input field bottom border
         user_gradient,
         text_color, 
         text_color, 
         "rgb(200,200,200)", #TODO deal with the bug that doesn't allow dynmaic color change for the two size spinboxes
         text_color,
         button_color,
         button_color,
         button_after_pressed,
         button_after_pressed,
         button_after_pressed,
         light_accent,
         light_accent,
         light_accent,
         text_color,
         user_gradient,
         light_accent,
         light_accent,
         user_gradient,
         user_gradient,
         user_gradient,
      )
  # print(stylesheet)
  return stylesheet


update_color_schemes(start_color, end_color)
