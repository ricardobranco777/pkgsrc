$NetBSD: patch-pytest__lazyfixture.py,v 1.1 2024/07/14 06:07:13 wiz Exp $

Fix compatibility with pytest 8.
https://github.com/TvoroG/pytest-lazy-fixture/issues/65

diff --git a/pytest_lazyfixture.py b/pytest_lazyfixture.py
index abf5db5..df83ce7 100644
--- pytest_lazyfixture.py.orig	2020-02-01 17:28:55.000000000 +0000
+++ pytest_lazyfixture.py
@@ -71,14 +71,13 @@ def pytest_make_parametrize_id(config, v
 def pytest_generate_tests(metafunc):
     yield
 
-    normalize_metafunc_calls(metafunc, 'funcargs')
-    normalize_metafunc_calls(metafunc, 'params')
+    normalize_metafunc_calls(metafunc)
 
 
-def normalize_metafunc_calls(metafunc, valtype, used_keys=None):
+def normalize_metafunc_calls(metafunc, used_keys=None):
     newcalls = []
     for callspec in metafunc._calls:
-        calls = normalize_call(callspec, metafunc, valtype, used_keys)
+        calls = normalize_call(callspec, metafunc, used_keys)
         newcalls.extend(calls)
     metafunc._calls = newcalls
 
@@ -98,17 +97,21 @@ def copy_metafunc(metafunc):
     return copied
 
 
-def normalize_call(callspec, metafunc, valtype, used_keys):
+def normalize_call(callspec, metafunc, used_keys):
     fm = metafunc.config.pluginmanager.get_plugin('funcmanage')
 
     used_keys = used_keys or set()
-    valtype_keys = set(getattr(callspec, valtype).keys()) - used_keys
+    keys = set(callspec.params.keys()) - used_keys
+    print(used_keys, keys)
 
-    for arg in valtype_keys:
-        val = getattr(callspec, valtype)[arg]
+    for arg in keys:
+        val = callspec.params[arg]
         if is_lazy_fixture(val):
             try:
-                _, fixturenames_closure, arg2fixturedefs = fm.getfixtureclosure([val.name], metafunc.definition.parent)
+                if pytest.version_tuple >= (8, 0, 0):
+                    fixturenames_closure, arg2fixturedefs = fm.getfixtureclosure(metafunc.definition.parent, [val.name], {})
+                else:
+                    _, fixturenames_closure, arg2fixturedefs = fm.getfixtureclosure([val.name], metafunc.definition.parent)
             except ValueError:
                 # 3.6.0 <= pytest < 3.7.0; `FixtureManager.getfixtureclosure` returns 2 values
                 fixturenames_closure, arg2fixturedefs = fm.getfixtureclosure([val.name], metafunc.definition.parent)
@@ -117,14 +120,14 @@ def normalize_call(callspec, metafunc, v
                 fixturenames_closure, arg2fixturedefs = fm.getfixtureclosure([val.name], current_node)
 
             extra_fixturenames = [fname for fname in fixturenames_closure
-                                  if fname not in callspec.params and fname not in callspec.funcargs]
+                                  if fname not in callspec.params]# and fname not in callspec.funcargs]
 
             newmetafunc = copy_metafunc(metafunc)
             newmetafunc.fixturenames = extra_fixturenames
             newmetafunc._arg2fixturedefs.update(arg2fixturedefs)
             newmetafunc._calls = [callspec]
             fm.pytest_generate_tests(newmetafunc)
-            normalize_metafunc_calls(newmetafunc, valtype, used_keys | set([arg]))
+            normalize_metafunc_calls(newmetafunc, used_keys | set([arg]))
             return newmetafunc._calls
 
         used_keys.add(arg)
