import pandas as pd
import wx
import wx.grid

class FoodDetails(wx.Frame):
    def __init__(self, parent, col_labels):
        wx.Frame.__init__(self, parent, title="Food Details", size=(400, 300))

        self.grid = wx.grid.Grid(self)
        self.grid.CreateGrid(0, len(col_labels))

        for col_index, label in enumerate(col_labels):
            self.grid.SetColLabelValue(col_index, label)

        self.total_row_index = 0
        self.grid.AppendRows(1)
        self.grid.SetCellValue(self.total_row_index, 0, "Total")

        self.grid.SetReadOnly(self.total_row_index, 0, True)

        self.grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.on_row_click)

    def append_row(self, food_data):
        current_rows = self.grid.GetNumberRows()
        self.grid.InsertRows(pos=current_rows, numRows=1)

        for col_index, data in enumerate(food_data):
            self.grid.SetCellValue(current_rows, col_index, data)

        self.update_totals()

    def on_row_click(self, event):
        row_index = event.GetRow()

        if row_index == self.total_row_index:
            return

        self.grid.DeleteRows(pos=row_index, numRows=1)
        self.update_totals()

    def update_totals(self):
        num_rows = self.grid.GetNumberRows() - 1
        num_cols = self.grid.GetNumberCols()

        totals = [0.0] * num_cols

        for row in range(1, num_rows + 1):
            for col in range(1, num_cols):
                try:
                    value = float(self.grid.GetCellValue(row, col))
                    totals[col] += value
                except ValueError:
                    pass

        for col in range(1, num_cols):
            self.grid.SetCellValue(self.total_row_index, col, str(round(totals[col], 3)))

        for col in range(num_cols):
            self.grid.SetReadOnly(self.total_row_index, col, True)

class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="Vitamin Search", pos=wx.DefaultPosition, size=wx.Size(873, 423), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.dataset = pd.read_csv('Food_Nutrition_Dataset.csv')
        self.vitamins = self.dataset.columns[13:25]

        bSizer3 = wx.BoxSizer(wx.VERTICAL)
        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"Food Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        bSizer4.Add(self.m_staticText7, 0, wx.ALL, 5)

        self.m_textCtrl7 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_textCtrl7, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"Select Filter Option", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText4.Wrap(-1)
        bSizer4.Add(self.m_staticText4, 0, wx.ALL, 5)

        m_choice1Choices = [
            "Caloric Value",
            "Fat",
            "Saturated Fats",
            "Monounsaturated Fats",
            "Polyunsaturated Fats",
            "Carbohydrates",
            "Sugars",
            "Protein",
            "Dietary Fiber",
            "Cholesterol",
            "Sodium",
            "Water",
            "Vitamin A",
            "Vitamin B1",
            "Vitamin B11",
            "Vitamin B12",
            "Vitamin B2",
            "Vitamin B3",
            "Vitamin B5",
            "Vitamin B6",
            "Vitamin C",
            "Vitamin D",
            "Vitamin E",
            "Vitamin K",
            "Calcium",
            "Copper",
            "Iron",
            "Magnesium",
            "Manganese",
            "Phosphorus",
            "Potassium",
            "Selenium",
            "Zinc",
            "Nutrition Density"
        ]

        self.m_choice1 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0)
        self.m_choice1.SetSelection(0)
        bSizer4.Add(self.m_choice1, 0, wx.ALL, 5)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Min", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer4.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_textCtrl5, 0, wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"Max", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer4.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.m_textCtrl6 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_textCtrl6, 0, wx.ALL, 5)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"Sort Order", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        bSizer4.Add(self.m_staticText8, 0, wx.ALL, 5)

        sort_order_choices = ["Ascending", "Descending"]
        self.m_choice_sort = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sort_order_choices, 0)
        self.m_choice_sort.SetSelection(0)
        bSizer4.Add(self.m_choice_sort, 0, wx.ALL, 5)

        self.m_staticText_level = wx.StaticText(self, wx.ID_ANY, u"Level Filter", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_level.Wrap(-1)
        bSizer4.Add(self.m_staticText_level, 0, wx.ALL, 5)

        level_filter_choices = ["None", "Low", "Medium", "High"]
        self.m_choice_level = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, level_filter_choices, 0)
        self.m_choice_level.SetSelection(0)
        bSizer4.Add(self.m_choice_level, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button3, 0, wx.ALL, 5)

        bSizer3.Add(bSizer4, 0, wx.EXPAND, 5)

        self.result_count_text = wx.StaticText(self, wx.ID_ANY, u"Results found: 0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.result_count_text.Wrap(-1)
        bSizer3.Add(self.result_count_text, 0, wx.ALL, 5)

        self.m_grid2 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_grid2.CreateGrid(0, 9)
        self.m_grid2.EnableEditing(True)
        self.m_grid2.EnableGridLines(True)
        self.m_grid2.SetMargins(0, 0)
        self.m_grid2.EnableDragColMove(False)
        self.m_grid2.EnableDragColSize(True)
        self.m_grid2.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        self.m_grid2.EnableDragRowSize(True)
        self.m_grid2.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        self.m_grid2.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)

        bSizer3.Add(self.m_grid2, 0, wx.ALL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        self.m_button3.Bind(wx.EVT_BUTTON, self.on_search)
        self.m_grid2.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.on_row_click)

    def on_search(self, event):
        selected_vitamin = self.m_choice1.GetStringSelection()
        food_name = self.m_textCtrl7.GetValue().lower()

        min_value = None
        max_value = None

        if self.m_textCtrl5.GetValue():
            try:
                min_value = float(self.m_textCtrl5.GetValue())
            except ValueError:
                wx.MessageBox("Please enter a valid numeric value for Min.", "Error", wx.OK | wx.ICON_ERROR)
                return

        if self.m_textCtrl6.GetValue():
            try:
                max_value = float(self.m_textCtrl6.GetValue())
            except ValueError:
                wx.MessageBox("Please enter a valid numeric value for Max.", "Error", wx.OK | wx.ICON_ERROR)
                return

        if selected_vitamin == "Food":
            filtered_data = self.dataset[self.dataset['food'].str.lower().str.contains(food_name, na=False)]
        else:
            filtered_data = self.dataset[(self.dataset[selected_vitamin].notna()) & (self.dataset['food'].str.lower().str.contains(food_name, na=False))]

            if min_value is not None:
                filtered_data = filtered_data[filtered_data[selected_vitamin] >= min_value]
            if max_value is not None:
                filtered_data = filtered_data[filtered_data[selected_vitamin] <= max_value]

        sort_order = self.m_choice_sort.GetStringSelection()
        if sort_order == "Ascending":
            filtered_data = filtered_data.sort_values(by=selected_vitamin)
        else:
            filtered_data = filtered_data.sort_values(by=selected_vitamin, ascending=False)

        level_filter = self.m_choice_level.GetStringSelection()
        if level_filter != "None":
            highest_value = filtered_data[selected_vitamin].max() if not filtered_data.empty else 0

            low_threshold = highest_value * 0.33
            high_threshold = highest_value * 0.66

            if level_filter == "Low":
                filtered_data = filtered_data[filtered_data[selected_vitamin] < low_threshold]
            elif level_filter == "Medium":
                filtered_data = filtered_data[(filtered_data[selected_vitamin] >= low_threshold) & (filtered_data[selected_vitamin] <= high_threshold)]
            elif level_filter == "High":
                filtered_data = filtered_data[filtered_data[selected_vitamin] > high_threshold]

        self.result_count_text.SetLabel(f"Results found: {len(filtered_data)}")

        self.populate_grid(filtered_data)

    def populate_grid(self, filtered_data):
        self.m_grid2.ClearGrid()

        num_rows = len(filtered_data)
        num_cols = len(filtered_data.columns)

        if num_rows > self.m_grid2.GetNumberRows():
            self.m_grid2.AppendRows(num_rows - self.m_grid2.GetNumberRows())
        elif num_rows < self.m_grid2.GetNumberRows():
            self.m_grid2.DeleteRows(num_rows, self.m_grid2.GetNumberRows() - num_rows)

        if num_cols > self.m_grid2.GetNumberCols():
            self.m_grid2.AppendCols(num_cols - self.m_grid2.GetNumberCols())
        elif num_cols < self.m_grid2.GetNumberCols():
            self.m_grid2.DeleteCols(num_cols, self.m_grid2.GetNumberCols() - num_cols)

        for col_idx, col_name in enumerate(filtered_data.columns):
            self.m_grid2.SetColLabelValue(col_idx, col_name)

        for row_idx, row_data in enumerate(filtered_data.iterrows()):
            for col_idx, value in enumerate(row_data[1]):
                self.m_grid2.SetCellValue(row_idx, col_idx, str(value))

        self.m_grid2.Fit()
        self.Layout()

    def on_row_click(self, event):
        row_index = event.GetRow()

        food_data = [self.m_grid2.GetCellValue(row_index, col_index) for col_index in range(self.m_grid2.GetNumberCols())]

        col_labels = [self.m_grid2.GetColLabelValue(col_index) for col_index in range(self.m_grid2.GetNumberCols())]

        if hasattr(self, 'open_window') and self.open_window is not None:
            self.open_window.append_row(food_data)
        else:
            self.open_window = FoodDetails(self, col_labels)
            self.open_window.append_row(food_data)
            self.open_window.Show()

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None)
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
