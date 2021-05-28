#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Create interactive pie charts and bar charts together with radio buttons.

Create radio buttons for the user to choose.
Then create and display pie charts and bar charts according to the options
of radio buttons.

"""

__author__ = "Group No.18 in DSP of Lanzhou University: Yuming Chen, Huiyi Liu"
__copyright__ = "Copyright 2020, Study Project in Lanzhou University , China"
__license__ = "GPL V3"
__maintainer__ = "Yuming Chen"
__email__ = ["chenym18@lzu.edu.cn", "liuhuiyi18@lzu.edu.cn"]
__status__ = "Experimental"

from matplotlib.widgets import RadioButtons
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import numpy as np


class SelectionBox(RadioButtons):
    """
    This is a custom class inherited from the "matplotlib.widgets.RadioButtons".

    For the buttons to remain responsive you must keep a reference to this
    object.

    Connect to the SelectionBox with the `.on_clicked` method.

    Attributes
    ----------
    ax : `matplotlib.axes.Axes`
        The parent axes for the widget.
    activecolor : color
        The color of the selected button.
    labels : list of `.Text`
        The button labels.
    circles : list of `~.patches.Circle`
        The buttons.
    value_selected : str
        The label text of the currently selected button.
    """

    def __init__(self, ax: Axes, **params):
        """
        Add selection box an `matplotlib.axes.Axes`.

        Parameters
        ----------
        ax : `matplotlib.axes.Axes`
            The axes to add the buttons to.
        labels : list of str
            The button labels.
        active : int
            The index of the initially selected button.
        activecolor : color
            The color of the selected button.
        """
        self.ax = ax
        self.ax.clear()
        for spine in self.ax.spines:
            self.ax.spines[spine].set_visible(False)
        self.ax.set(aspect='equal')
        super().__init__(ax, **params)

    def set_buttons(self, radius: float = 0.02, offset: float = 0.06, circleprops: dict = None, textprops: dict = None):
        """
        Set the style of buttons.

        Parameters
        ----------
        radius: float
            The radius of buttons.
        offset: float
            The offset between bottom and labels.
        circleprops : dict, optional
            The properties of the style of each button's circle.
        textprops : dict, optional
            The properties of the style of each button's label.
        """
        if circleprops is None:
            circleprops = {}
        if textprops is None:
            textprops = {}
        for circle, label in zip(self.circles, self.labels):
            x, y = circle.get_center()
            circle.set_radius(radius)
            circle.set_center((x + offset, y))
            circle.set(**circleprops)
            label.set(**textprops)


class SelectionPlot:
    """
    This is a custom class which is to create bar charts and pie charts
    according to the options of ratio buttons.

    Reffered to the options selected by the user, the class create the plot
    based on the corresponding data.

    Attributes
    ----------
    ax : `matplotlib.axes.Axes`
        The parent axes for the plot.
    """

    def __init__(self, ax: Axes,
                 labels: pd.Series,
                 data: pd.DataFrame,
                 is_pie: bool = True,
                 title: str = '{}',
                 font_dicts: dict = None,
                 **params):
        """

        Parameters
        ----------
        ax : `matplotlib.axes.Axes`
            The axes to add the plot to.
        labels : `pd.Series`
            The label of plot.
        data : `pd.DataFrame`
            The data of plot.
        is_pie : bool
            If true, draw the pie plot, else draw the bar plot.
        title : str
            Title of plot.
        font_dicts: dict
            The dictionary of font style.
            ==========   ======================================================
            Key          Description
            ==========   ======================================================
            global      The style of all the fonts
            title       The style of title
            label       The style of label
            value       The style of value
            ==========   ======================================================
        **params :
            The parameters of the plot.
        """
        if not font_dicts:
            font_dicts = {'global': {'family': 'Times New Roman'},
                          'title': {'weight': 'black', 'size': 14},
                          'label': {},
                          'value': {}}
        self.ax = ax
        self.__labels = labels
        self.__data = data
        self.__is_pie = is_pie
        self.__title = title
        self.__params = params
        self.__font_dicts = font_dicts
        self.__rc = rc('font', **self.__font_dicts['global'])
        self.__init_plot()


    def __init_plot(self):
        """
        Initialize the plot, setting x_axis if the type of graph is bar chart.
        """
        # Make the border of plot invisible
        for position in self.ax.spines:
            if not self.__is_pie and position == "bottom":
                continue
            self.ax.spines[position].set_visible(False)
        # Init the plot
        self.draw('all')

    def draw(self, value):
        """
        Creating corresponding plot based on the option of the radio button.

        Parameters
        ----------
        value : str
            The label text of the currently selected button.
        """
        self.ax.clear()
        self.ax.set_title(self.__title.format(value + ' drugs' if value == 'all' else value),
                          fontdict=self.__font_dicts['title'])
        # Set y-axis
        self.ax.set_yticks([])
        # Draw the pie plot
        if self.__is_pie:
            pctdistance = 1.09 if value == 'all' else 0.6
            labeldistance = 1.2 if value == 'all' else 1.1
            pie = self.ax.pie(x=self.__data.loc[value][self.__data.loc[value] != 0],
                              labels=self.__data.loc[value][self.__data.loc[value] != 0].index,
                              autopct='%1.0f%%',
                              pctdistance=pctdistance,
                              labeldistance=labeldistance,
                              **self.__params)
            for label, value in zip(pie[1], pie[2]):
                label.set(**self.__font_dicts['label'])
                value.set(**self.__font_dicts['value'])

        # Draw the bar plot
        else:
            # Set y-axis
            max_value = max(self.__data[filter(lambda x: x != 'all', self.__data.columns)].max()) \
                if value != 'all' \
                else max(self.__data[value])
            self.ax.set_ylim(0, max_value * 1.1)
            # Set x-axis
            self.ax.set_xlim(-0.6, len(self.__labels) - 0.5)
            self.ax.tick_params(bottom=False, top=False, left=False, right=False)
            self.ax.set_xticklabels(self.__labels,
                                    fontdict=self.__font_dicts['label'])
            # Draw the bar plot
            rects = self.ax.bar(x=self.__labels,
                                height=self.__data[value],
                                **self.__params)
            # Add value on the top of each bar
            for rect in rects:
                height = rect.get_height()
                if height:
                    self.ax.annotate('{}'.format(height),
                                     xy=(rect.get_x() + rect.get_width() / 2, height),
                                     xytext=(0, 1),
                                     textcoords="offset points",
                                     ha='center',
                                     va='bottom',
                                     **self.__font_dicts['value'])
        return self.ax


if __name__ == "__main__":
    from matplotlib.gridspec import GridSpec
    from matplotlib import cm
    from copy import deepcopy

    df = pd.read_csv('data.csv', index_col=0)
    pie_data = deepcopy(df)
    sum_ = df.sum(axis=0)
    sum_.name = 'all'
    pie_data = pie_data.append(sum_)
    pie_labels = pie_data.index
    bar_data = deepcopy(df)
    bar_data['all'] = df.sum(axis=1)
    bar_labels = bar_data.index

    fig = plt.figure(figsize=(15, 12))
    gs = GridSpec(2, 16, figure=fig)

    pie_ax = fig.add_subplot(gs[0, :8])
    pie_select_ax = fig.add_subplot(gs[0, -8:])
    pie_props = {
        'ax': pie_ax,
        'labels': pie_labels,
        'data': pie_data,
        'is_pie': True,
        'title': "the disease groups as side effects in drug interaction with |{}|",
        'font_dicts': None,
        'colors': cm.Blues(np.arange(len(pie_labels)) / len(pie_labels) + 0.2)
    }
    pie = SelectionPlot(**pie_props)
    pie_sb = SelectionBox(ax=pie_select_ax,
                          labels=pie_data.index,
                          active=len(pie_data.index) - 1,
                          activecolor='#274279')
    pie_sb.set_buttons(circleprops={'fc': 'white', 'ec': '#274279'})
    pie_sb.on_clicked(pie.draw)

    bar_ax = fig.add_subplot(gs[1, :-3])
    bar_select_ax = fig.add_subplot(gs[1, -3:])
    bar_props = {
        'ax': bar_ax,
        'labels': bar_labels,
        'data': bar_data,
        'is_pie': False,
        'title': "The number of drugs causing |{}| in drug interaction",
        'font_dicts': None,
        'width': 0.3
    }
    bar = SelectionPlot(**bar_props)
    bar_sb = SelectionBox(ax=bar_select_ax,
                          labels=bar_data.columns,
                          active=len(bar_data.columns) - 1,
                          activecolor='#274279')
    bar_sb.set_buttons(circleprops={'fc': 'white', 'ec': '#274279'})
    bar_sb.on_clicked(bar.draw)
    plt.ion()
    plt.pause(0)
