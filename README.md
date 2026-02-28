# 鸿蒙开发者文档抓取工具

用于抓取华为鸿蒙开发者文档站点 (https://developer.huawei.com/consumer/cn/doc/) 的工具，将文档转换为Markdown格式存储。

## 抓取结果

| 类别 | 文件数量 | 说明 |
|------|----------|------|
| **指南 (Guides)** | 4,062 个 | 开发指南、最佳实践、常见问题等 |
| **API参考 (References)** | 5,633 个 | ArkTS/C/JS API接口文档 |
| **总计** | **9,695 个** | Markdown 文档 |

## 用户使用指导

### 查询API文档

1. **按功能模块查询**
   - 进入 `harmonyos-docs-full/references/` 目录
   - 根据功能模块分类查找（如：应用服务/、系统/、媒体/等）
   - 例如：查询屏幕时间守护API → `应用服务/Screen Time Guard Kit（屏幕时间守护服务）/`

2. **按权限查询**
   - 权限列表文档：`references/系统/安全/程序访问控制/应用权限管控/应用权限列表/受限开放权限.md`
   - 包含所有 `ohos.permission.*` 权限的详细说明

3. **搜索关键词**
   ```bash
   # Windows PowerShell
   cd harmonyos-docs-full/references
   Select-String -Path "*.md" -Pattern "剪贴板" | Select-Object -First 10

   # 或使用任何文本搜索工具（如VSCode搜索、Everything等）
   ```

### 查询开发指南

1. **快速入门**
   - 路径：`guides/基础入门/快速入门/`
   - 包含：开发准备、构建第一个应用等

2. **按Kit查询**
   - 每个服务Kit都有独立的目录
   - 例如：`guides/应用服务/Screen Time Guard Kit（屏幕时间守护服务）/`
   - 包含：概述、开发步骤、API说明、示例代码

3. **常见问题排查**
   - 路径：`guides/编写与调试应用/`
   - 包含：调试技巧、错误排查、性能优化

### 知识库使用建议

**创建2个知识库**，分别对应指南和API参考：

| 知识库名称 | 文档来源 | 适用场景 |
|-----------|----------|----------|
| HarmonyOS 开发指南完整版 | `guides_all.md` | 查询开发流程、功能实现、最佳实践、问题排查 |
| HarmonyOS API参考手册完整版 | `references_all.md` | 查询API接口、参数定义、权限要求、错误码 |

**使用技巧**：
- 开发新功能时，先查"开发指南"了解实现方式，再查"API参考"获取接口细节
- 遇到错误码时，在"API参考"中搜索错误码数字
- 需要申请权限时，在"API参考"中搜索权限名称获取申请条件和场景说明

## 常见API快速查询

### 屏幕时间守护 (Screen Time Guard Kit)

**用途**：应用使用时长管理、屏幕访问控制

**权限**: `ohos.permission.MANAGE_SCREEN_TIME_GUARD` (system_basic级别)

**文档路径**:
- 指南：`guides/应用服务/Screen Time Guard Kit（屏幕时间守护服务）/`
- API：`references/应用服务/Screen Time Guard Kit（屏幕时间守护服务）/ArkTS API/`

**快速代码**:
```typescript
import { guardService } from '@kit.ScreenTimeGuardKit';

// 请求用户授权
await guardService.requestUserAuth(context);

// 添加时间管控策略
const strategy: guardService.GuardStrategy = {
  name: "LimitAppUse",
  timeStrategy: { type: guardService.TimeStrategyType.TOTAL_DURATION_TYPE, totalDuration: 120 },
  appInfo: { appTokens: selectedTokens },
  appRestrictionType: guardService.RestrictionType.BLOCKLIST_TYPE
};
await guardService.addGuardStrategy(strategy);
```

### 剪贴板 (Pasteboard)

**用途**：系统剪贴板读写

**权限**: `ohos.permission.READ_PASTEBOARD` (读取需要，写入不需要)

**文档路径**:
- 指南：`guides/系统/基础功能/Basic Services Kit（基础服务）/剪贴板服务/`
- API：`references/应用开发/js-apis-pasteboard.md`

**快速代码**:
```typescript
import { pasteboard } from '@kit.BasicServicesKit';

// 写入剪贴板（无需权限）
const systemPasteboard = pasteboard.getSystemPasteboard();
let pasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'Hello');
await systemPasteboard.setData(pasteData);

// 读取剪贴板（需要权限或使用PasteButton控件）
const data = await systemPasteboard.getData();
let text = data.getPrimaryText();
```

## 目录结构

```
harmonyos-docs-full/
├── guides/                    # 指南文档 (按目录层级结构)
│   ├── AI/                    # AI开发 (789个)
│   ├── 应用框架/              # 应用框架 (747个)
│   ├── 系统/                  # 系统开发 (646个)
│   ├── 应用服务/              # 应用服务 (639个)
│   ├── 编写与调试应用/        # 调试相关 (375个)
│   ├── 媒体/                  # 媒体开发 (252个)
│   ├── 图形/                  # 图形开发 (151个)
│   ├── NDK开发/               # Native开发 (113个)
│   ├── 开发环境搭建/          # 环境配置 (102个)
│   └── ...
│
├── references/                # API参考文档 (按目录层级结构)
│   ├── 应用开发/              # 应用开发API (3318个)
│   ├── 应用框架/              # 框架API (1180个)
│   ├── 系统/                  # 系统API (416个)
│   ├── 媒体/                  # 媒体API (242个)
│   ├── 应用服务/              # 服务API (239个)
│   ├── 图形/                  # 图形API (133个)
│   ├── AI/                    # AI API (59个)
│   └── ...
│
├── guides_mapping.json         # 指南URL映射表
├── url_mapping.json            # API参考URL映射表
└── progress.json               # 爬取进度记录
```

## 详细数据统计

### 指南 (Guides) 分类统计

| 分类 | 文件数 | 分类 | 文件数 |
|------|--------|------|--------|
| AI | 789 | 基础入门 | 38 |
| 应用框架 | 747 | 优化应用性能 | 28 |
| 系统 | 646 | 使用AI智能辅助编程 | 20 |
| 应用服务 | 639 | 应用测试 | 15 |
| 编写与调试应用 | 375 | 自由流转 | 7 |
| 媒体 | 252 | 应用开发准备 | 1 |
| 图形 | 151 | 发布应用 | 1 |
| NDK开发 | 113 | 一次开发，多端部署 | 1 |
| 开发环境搭建 | 102 | - | - |
| 应用体验建议 | 47 | **总计** | **4,062** |
| 构建应用 | 46 | | |
| 命令行工具 | 44 | | |

**指南数据量**：36 MB，约 355,488 行，2,800万+ 字符

### API参考 (References) 分类统计

| 分类 | 文件数 | 分类 | 文件数 |
|------|--------|------|--------|
| 应用开发 | 3,318 | 图形 | 133 |
| 应用框架 | 1,180 | AI | 59 |
| 系统 | 416 | 标准库 | 26 |
| 媒体 | 242 | 公共基础能力 | 17 |
| 应用服务 | 239 | API参考概述 | 3 |
| **总计** | **5,633** | | |

**参考数据量**：87 MB，约 700,000+ 行，5,500万+ 字符

## 工具脚本

```
harmony-developer-docs-fetcher/
├── merge_docs.py               # 文档合并工具 (生成超大MD文件)
└── parser/                     # HTML转Markdown解析模块
```

## 文档合并

运行 `merge_docs.py` 可将目录下的文档按结构合并为超大MD文件：

```bash
python merge_docs.py
```

生成文件：
- `guides_all.md` - 指南完整合并版 (~28 MB)
- `references_all.md` - API参考完整合并版 (~75 MB)

## 知识库配置建议

### 知识库1：开发指南

```
名称: HarmonyOS 开发指南完整版
描述: 鸿蒙系统官方开发指南文档，包含20个主要领域：基础入门、ArkTS语言开发、应用框架、
      系统API（安全、网络、媒体、图形、AI）、应用服务（账号、支付、推送、地图、广告、
      屏幕时间守护等）、测试、工具使用、跨设备流转、应用模型、权限管理、UI开发、
      数据管理等。提供快速入门、开发准备、最佳实践、常见问题解答等完整开发指导。
```

### 知识库2：API参考

```
名称: HarmonyOS API参考手册完整版
描述: 鸿蒙系统完整API参考文档，涵盖10大模块的详细接口说明：应用开发、应用框架、
      系统与安全、网络、媒体、图形、应用服务、AI能力、基础库等。包含ArkTS API、
      C API、JS API的接口定义、参数说明、返回值、错误码、系统能力、权限要求、
      起始版本、设备支持范围等完整技术细节。
```

## 技术实现

- **抓取方式**: API方式调用 `getCatalogTree` 接口获取完整目录树
- **渲染引擎**: Playwright + Chromium Headless
- **内容提取**: `.markdown-body` 选择器提取正文
- **格式转换**: 自定义HTML转Markdown模块
- **代码格式化**: jsbeautifier 自动格式化代码块

## 系统要求

```bash
pip install playwright
playwright install chromium
```

## 更新日志

- **2026-02-27**: 完成所有文档抓取 (9,695 个文件)
- **2026-02-27**: 代码块格式化完成
- **2026-02-28**: 生成完整合并版文档工具

## 许可证

本项目仅供学习交流使用，文档版权归原作者所有。
