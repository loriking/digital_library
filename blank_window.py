import tkinter as tk
from tkinter import ttk


def show_window(window, tall):
    scollresources = ttk.Scrollbar(window)
    scollresources.grid(column=2, row=2, sticky=tk.N + tk.S + tk.W)

    resource_list2 = ttk.Treeview(window, height=tall)
    resource_list2['columns'] = ('', '', '', '', '', '')

    scollresources.configure(orient="vertical", command=resource_list2.yview)
    resource_list2.configure(yscrollcommand=scollresources.set)

    resource_list2.column('#0', minwidth=0, width=0)
    resource_list2.column('0', width=240, anchor='w')
    resource_list2.column('1', width=150, anchor='w')
    resource_list2.column('2', width=75, anchor='w')
    resource_list2.column('3', width=75, anchor='w')
    resource_list2.column('4', width=100, anchor='w')
    resource_list2.column('5', width=220, anchor='w')
    resource_list2.grid(column=0, row=2, sticky=tk.W + tk.N + tk.E)

    resource_list2.heading('0', anchor='w')
    resource_list2.heading('1', anchor='w')
    resource_list2.heading('2', anchor='w')
    resource_list2.heading('3', anchor='w')
    resource_list2.heading('4', anchor='w')
    resource_list2.heading('5', anchor='w')
