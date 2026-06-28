# 401 Review Repository Guide

这是一个用于复习 **ECE4010J / 401 概率统计相关内容** 的自用仓库。

本仓库的核心目标不是写教材，而是维护一份可以在考试中快速查阅的 **paper-based cheating sheet**。由于 cheating sheet 的页数没有严格限制，维护时不需要为了追求极端简洁而删掉关键解释、符号含义、适用条件或考试提醒；更重要的是让打印后的材料在考场上能直接看懂、直接套用。

---

## 1. 最重要的文件

当前主要维护文件是根目录下的：

```text
cheating_sheet.md
```

用户平时主要只看这个文件。其他文件只是辅助资料、归档材料或自动化脚本。

`cheating_sheet.md` 的定位是：

```text
考试速查表 + 公式表 + 题型模板 + 符号/缩写说明 + Worked Examples
```

其中最前面的 **Symbol / Abbreviation Reference** 用于解释常见概率符号和英文缩写，例如：

```text
p_X(x), f_X(x), F_X(x), E[X], Var(X), E[g(X)],
f_{X,Y}(x,y), f_{X|Y}(x|y), R(t), h(t), M_X(t), iid, PMF, PDF, CDF, LOTUS, MGF
```

这部分非常重要，因为用户备考时经常不是不会算，而是先卡在符号含义上。

---

## 2. 考试材料限制

非常重要：

```text
考试只能携带纸质材料。
```

因此，`cheating_sheet.md` 里虽然可以保留 Markdown 链接，例如：

```markdown
[C-RV-001](#c-rv-001)
[EX-JOINT-001](#ex-joint-001)
```

但不能依赖链接跳转作为主要索引方式。因为打印成纸质材料后，链接不会生效。

所以主索引应尽量依赖 **可打印、可肉眼查找的编号系统**：

```text
Concept ID: C-模块-编号
Example ID: EX-模块-编号
```

不过从现在开始，**新增例题不再强制同步维护 Quick Index、Concept-to-Example Map、Tag Index、Related Examples**。这些已有映射关系保留，但不作为新增例题的强制维护负担。

---

## 3. 文档设计原则

### 3.1 考试速查优先，但不要过度压缩

这不是教材，也不是完整讲义。优先保留：

- 公式；
- 符号含义；
- 英文缩写解释；
- 适用条件；
- support / valid range；
- 题型识别关键词；
- 解题模板；
- 常见陷阱；
- 结构化例题。

不要为了“短”而删掉会影响考场理解的内容。特别是以下内容不应被省略：

- \(X\) 和 \(x\) 的区别；
- \(p_X(x)\)、\(f_X(x)\)、\(F_X(x)\) 的区别；
- PMF / PDF / CDF / LOTUS / MGF / iid 的完整含义；
- rate 和 scale 的区别；
- transformation 中 support 和 absolute value 的提醒；
- joint PDF 中 marginal / conditional 的分母到底是谁。

原则是：

```text
可以详细，不要空泛；可以多页，不要漏关键条件。
```

### 3.2 概念和例题分离

概念区只放：

- 定义；
- 什么时候用；
- 公式；
- 考试模板；
- 常见陷阱；
- 必要的迷你解释。

完整例题必须放在 `Worked Examples` 区域。

### 3.3 稳定 ID

已有 ID 一旦建立，后续不要因为重排章节而修改。

原因：

- 用户会在纸质材料上通过编号查找；
- 后续 AI 维护时也依赖这些编号；
- 改 ID 会破坏旧笔记和交叉引用。

如果是通过自动脚本新增的例题，可以使用：

```text
EX-AUTO-001, EX-AUTO-002, ...
```

如果确实想手动指定某个编号，也可以用：

```text
EX-DIST-005
EX-TRANS-006
EX-JOINT-004
```

---

## 4. `cheating_sheet.md` 的固定结构

主文件建议保持以下结构：

```markdown
# ECE4010J Midterm Cheating Sheet

## 0. Symbol / Abbreviation Reference
## 1. Quick Index
## 2. Concept-to-Example Map
## 3. Tag Index
## 4. How to Use This Sheet
## 5. Core Concepts
## 6. Exam Templates
## 7. Worked Examples
## 13. Common Traps
## 14. Final Self-check
```

说明：

- `Symbol / Abbreviation Reference` 放在最前面；
- `Core Concepts` 放概念、公式、模板和必要解释；
- `Exam Templates` 放可直接套用的解题流程；
- `Worked Examples` 放完整例题；
- `Common Traps` 放考试常见错误；
- `Final Self-check` 放考前自检清单。

---

## 5. 新增例题的推荐流程：自动插入

为了降低维护成本，新增例题默认使用脚本：

```text
scripts/add_worked_example.py
```

这个脚本只做一件事：

```text
把新的 worked example 插入到 cheating_sheet.md 的固定 marker 上方。
```

它不会强制更新：

- `Quick Index`
- `Concept-to-Example Map`
- `Tag Index`
- 相关概念的 `Related Examples`

这些旧映射关系可以继续保留；如果将来有精力再手动整理，但不再作为每次新增例题的必要步骤。

### 5.1 插入 marker

脚本使用下面的 marker：

```markdown
<!-- AUTO-WORKED-EXAMPLE-INSERT-BEFORE -->
```

规则：

```text
每次新增例题，都插入到这个 marker 的上方。
marker 本身保留在原地，方便下次继续插入。
```

如果 `cheating_sheet.md` 里暂时没有 marker，脚本会自动在 `## 13. Common Traps` 前创建一个 auto-insert zone。

### 5.2 使用方法

准备一个 markdown 文件作为题目本体，例如：

```text
docs/examples/EX-DIST-005-poisson-area-scaling.md
```

然后运行：

```bash
python scripts/add_worked_example.py \
  --title "Poisson Area Scaling" \
  --tags poisson area-scaling at-least-one \
  --body-file docs/examples/EX-DIST-005-poisson-area-scaling.md
```

如果不指定 `--id`，脚本会自动生成：

```text
EX-AUTO-001
EX-AUTO-002
...
```

如果想指定 ID：

```bash
python scripts/add_worked_example.py \
  --id EX-DIST-005 \
  --title "Poisson Area Scaling" \
  --tags poisson area-scaling at-least-one \
  --body-file docs/examples/EX-DIST-005-poisson-area-scaling.md
```

### 5.3 安全检查

脚本会检查：

- marker 是否唯一；
- Example ID 是否已经存在；
- anchor 是否重复；
- body file 是否存在；
- 插入后 marker 是否仍然保留；
- 插入后 anchor 是否只出现一次。

### 5.4 推荐提交流程

```bash
git checkout -b add-example
python scripts/add_worked_example.py \
  --id EX-DIST-005 \
  --title "Poisson Area Scaling" \
  --tags poisson area-scaling at-least-one \
  --body-file docs/examples/EX-DIST-005-poisson-area-scaling.md

git diff -- cheating_sheet.md
git diff --check
git add cheating_sheet.md
git commit -m "Add EX-DIST-005 Poisson area scaling"
```

---

## 6. 写作风格

建议风格：

- 中文解释为主；
- 关键英文术语保留；
- 英文缩写尽量给出 full name；
- 公式使用 LaTeX；
- 表格优先于长段落；
- 每个概念要写清：定义、适用条件、公式、模板、常见陷阱；
- 每个例题必须结构化；
- 重要提醒用 `> Warning:` 或 `> Exam Tip:`；
- 不要为了压缩页数删除关键解释，因为当前 cheating sheet 页数没有硬性限制。

推荐表达方式：

```markdown
| Symbol | English Name | 中文 | Meaning / Formula | Exam Usage |
|---|---|---|---|---|
```

或者：

```markdown
> Warning: 连续型随机变量 \(P(X=x)=0\)。PDF 的某个点的值不是概率。
```

---

## 7. 当前资料文件夹

辅助资料在：

```text
materials/
docs/examples/
scripts/
```

其中：

```text
materials/        归档和维护参考
docs/examples/    可复用 worked example markdown
scripts/          自动维护脚本
```

真正考试复习主要看：

```text
cheating_sheet.md
```

---

## 8. 给下一位 AI 的一句话指令

如果一个新的 AI 接手，请直接遵守下面这句话：

```text
请维护根目录 cheating_sheet.md。它是只能打印成纸质材料使用的考试速查表。新增例题时，优先使用 scripts/add_worked_example.py，将题目 markdown 插入到 AUTO-WORKED-EXAMPLE-INSERT-BEFORE marker 上方；不要每次都强制维护 Quick Index、Concept-to-Example Map、Tag Index 和 Related Examples。已有映射关系可以保留，必要时再手动整理。新增内容时，不要为了追求简洁而删掉关键符号解释、公式条件、support 或常见陷阱。
```
