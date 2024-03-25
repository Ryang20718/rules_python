# Copyright 2024 The Bazel Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Toolchain setup for precompiling py files into pyc."""
def _py_precompiler_toolchain_impl(ctx):
    return [platform_common.ToolchainInfo(
        interpreter = ctx.attr.interpreter,
        precompiler_src = ctx.attr.precompiler_src,
        python_version = ctx.attr.python_version,
    )]

py_precompiler_toolchain = rule(
    doc = """
    This rule exists so that the precompiler toolchain can be set for precompiling python files to pyc without.
    This cannot be a regular py_binary, otherwise there will be a circular dependency.
    """,
    implementation = _py_precompiler_toolchain_impl,
    attrs = {
        "interpreter": attr.label(cfg="exec"),
        "precompiler_src": attr.label(cfg="exec", default = Label("//tools/precompiler:precompiler.py")),
        "python_version": attr.string(doc = "python version. I.e 310 for python 3.10. Used for generating magic tag for pyc file", mandatory = True),
    },
    toolchains = ["//python:precompiler_toolchain_type"],
)
