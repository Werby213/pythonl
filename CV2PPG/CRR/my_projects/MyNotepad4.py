from tkinter import Tk, Scrollbar
from tkinterhtml import HtmlFrame

# Создаем главное окно
root = Tk()

# Создаем виджет HtmlFrame
html_frame = HtmlFrame(root)
html_frame.pack(fill="both", expand=True)

# HTML-код с подсветкой синтаксиса
html_code = """
<div class="highlight"><pre><span></span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">10</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;hello world&quot;</span><span class="p">)</span>
</pre></div>
"""

# Загружаем HTML-код в виджет HtmlFrame
html_frame.set_content(html_code)

# Запускаем главный цикл обработки событий
root.mainloop()