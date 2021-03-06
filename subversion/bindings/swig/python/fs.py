# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _fs

def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name) or (name == "thisown"):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import core
import delta

def svn_fs_version(*args):
    """svn_fs_version() -> svn_version_t"""
    return apply(_fs.svn_fs_version, args)
SVN_FS_CONFIG_BDB_TXN_NOSYNC = _fs.SVN_FS_CONFIG_BDB_TXN_NOSYNC
SVN_FS_CONFIG_BDB_LOG_AUTOREMOVE = _fs.SVN_FS_CONFIG_BDB_LOG_AUTOREMOVE
SVN_FS_CONFIG_FS_TYPE = _fs.SVN_FS_CONFIG_FS_TYPE
SVN_FS_TYPE_BDB = _fs.SVN_FS_TYPE_BDB
SVN_FS_TYPE_FSFS = _fs.SVN_FS_TYPE_FSFS
SVN_FS_CONFIG_PRE_1_4_COMPATIBLE = _fs.SVN_FS_CONFIG_PRE_1_4_COMPATIBLE

def svn_fs_initialize(*args):
    """svn_fs_initialize(apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_initialize, args)

def svn_fs_set_warning_func(*args):
    """svn_fs_set_warning_func(svn_fs_t fs, svn_fs_warning_callback_t warning, void warning_baton)"""
    return apply(_fs.svn_fs_set_warning_func, args)

def svn_fs_create(*args):
    """svn_fs_create(svn_fs_t fs_p, char path, apr_hash_t fs_config, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_create, args)

def svn_fs_open(*args):
    """svn_fs_open(svn_fs_t fs_p, char path, apr_hash_t config, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_open, args)

def svn_fs_type(*args):
    """svn_fs_type(char fs_type, char path, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_type, args)

def svn_fs_path(*args):
    """svn_fs_path(svn_fs_t fs, apr_pool_t pool) -> char"""
    return apply(_fs.svn_fs_path, args)

def svn_fs_delete_fs(*args):
    """svn_fs_delete_fs(char path, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_delete_fs, args)

def svn_fs_hotcopy(*args):
    """
    svn_fs_hotcopy(char src_path, char dest_path, svn_boolean_t clean, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_hotcopy, args)

def svn_fs_berkeley_recover(*args):
    """svn_fs_berkeley_recover(char path, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_berkeley_recover, args)

def svn_fs_berkeley_logfiles(*args):
    """
    svn_fs_berkeley_logfiles(apr_array_header_t logfiles, char path, svn_boolean_t only_unused, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_berkeley_logfiles, args)

def svn_fs_new(*args):
    """svn_fs_new(apr_hash_t fs_config, apr_pool_t pool) -> svn_fs_t"""
    return apply(_fs.svn_fs_new, args)

def svn_fs_create_berkeley(*args):
    """svn_fs_create_berkeley(svn_fs_t fs, char path) -> svn_error_t"""
    return apply(_fs.svn_fs_create_berkeley, args)

def svn_fs_open_berkeley(*args):
    """svn_fs_open_berkeley(svn_fs_t fs, char path) -> svn_error_t"""
    return apply(_fs.svn_fs_open_berkeley, args)

def svn_fs_berkeley_path(*args):
    """svn_fs_berkeley_path(svn_fs_t fs, apr_pool_t pool) -> char"""
    return apply(_fs.svn_fs_berkeley_path, args)

def svn_fs_delete_berkeley(*args):
    """svn_fs_delete_berkeley(char path, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_delete_berkeley, args)

def svn_fs_hotcopy_berkeley(*args):
    """
    svn_fs_hotcopy_berkeley(char src_path, char dest_path, svn_boolean_t clean_logs, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_hotcopy_berkeley, args)

def svn_fs_create_access(*args):
    """svn_fs_create_access(svn_fs_access_t access_ctx, char username, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_create_access, args)

def svn_fs_set_access(*args):
    """svn_fs_set_access(svn_fs_t fs, svn_fs_access_t access_ctx) -> svn_error_t"""
    return apply(_fs.svn_fs_set_access, args)

def svn_fs_get_access(*args):
    """svn_fs_get_access(svn_fs_access_t access_ctx, svn_fs_t fs) -> svn_error_t"""
    return apply(_fs.svn_fs_get_access, args)

def svn_fs_access_get_username(*args):
    """svn_fs_access_get_username(char username, svn_fs_access_t access_ctx) -> svn_error_t"""
    return apply(_fs.svn_fs_access_get_username, args)

def svn_fs_access_add_lock_token(*args):
    """svn_fs_access_add_lock_token(svn_fs_access_t access_ctx, char token) -> svn_error_t"""
    return apply(_fs.svn_fs_access_add_lock_token, args)

def svn_fs_compare_ids(*args):
    """svn_fs_compare_ids(svn_fs_id_t a, svn_fs_id_t b) -> int"""
    return apply(_fs.svn_fs_compare_ids, args)

def svn_fs_check_related(*args):
    """svn_fs_check_related(svn_fs_id_t id1, svn_fs_id_t id2) -> svn_boolean_t"""
    return apply(_fs.svn_fs_check_related, args)

def svn_fs_parse_id(*args):
    """svn_fs_parse_id(char data, apr_pool_t pool) -> svn_fs_id_t"""
    return apply(_fs.svn_fs_parse_id, args)

def svn_fs_unparse_id(*args):
    """svn_fs_unparse_id(svn_fs_id_t id, apr_pool_t pool) -> svn_string_t"""
    return apply(_fs.svn_fs_unparse_id, args)
SVN_FS_TXN_CHECK_OOD = _fs.SVN_FS_TXN_CHECK_OOD
SVN_FS_TXN_CHECK_LOCKS = _fs.SVN_FS_TXN_CHECK_LOCKS

def svn_fs_begin_txn2(*args):
    """
    svn_fs_begin_txn2(svn_fs_txn_t txn_p, svn_fs_t fs, svn_revnum_t rev, 
        apr_uint32_t flags, apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_begin_txn2, args)

def svn_fs_begin_txn(*args):
    """
    svn_fs_begin_txn(svn_fs_txn_t txn_p, svn_fs_t fs, svn_revnum_t rev, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_begin_txn, args)

def svn_fs_commit_txn(*args):
    """
    svn_fs_commit_txn(char conflict_p, svn_revnum_t new_rev, svn_fs_txn_t txn, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_commit_txn, args)

def svn_fs_abort_txn(*args):
    """svn_fs_abort_txn(svn_fs_txn_t txn, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_abort_txn, args)

def svn_fs_purge_txn(*args):
    """svn_fs_purge_txn(svn_fs_t fs, char txn_id, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_purge_txn, args)

def svn_fs_txn_name(*args):
    """svn_fs_txn_name(char name_p, svn_fs_txn_t txn, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_txn_name, args)

def svn_fs_txn_base_revision(*args):
    """svn_fs_txn_base_revision(svn_fs_txn_t txn) -> svn_revnum_t"""
    return apply(_fs.svn_fs_txn_base_revision, args)

def svn_fs_open_txn(*args):
    """svn_fs_open_txn(svn_fs_txn_t txn, svn_fs_t fs, char name, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_open_txn, args)

def svn_fs_list_transactions(*args):
    """svn_fs_list_transactions(apr_array_header_t names_p, svn_fs_t fs, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_list_transactions, args)

def svn_fs_txn_prop(*args):
    """
    svn_fs_txn_prop(svn_string_t value_p, svn_fs_txn_t txn, char propname, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_txn_prop, args)

def svn_fs_txn_proplist(*args):
    """svn_fs_txn_proplist(apr_hash_t table_p, svn_fs_txn_t txn, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_txn_proplist, args)

def svn_fs_change_txn_prop(*args):
    """svn_fs_change_txn_prop(svn_fs_txn_t txn, char name, svn_string_t value, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_change_txn_prop, args)

def svn_fs_revision_root(*args):
    """
    svn_fs_revision_root(svn_fs_root_t root_p, svn_fs_t fs, svn_revnum_t rev, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_revision_root, args)

def svn_fs_txn_root(*args):
    """svn_fs_txn_root(svn_fs_root_t root_p, svn_fs_txn_t txn, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_txn_root, args)

def svn_fs_close_root(*args):
    """svn_fs_close_root(svn_fs_root_t root)"""
    return apply(_fs.svn_fs_close_root, args)

def svn_fs_root_fs(*args):
    """svn_fs_root_fs(svn_fs_root_t root) -> svn_fs_t"""
    return apply(_fs.svn_fs_root_fs, args)

def svn_fs_is_txn_root(*args):
    """svn_fs_is_txn_root(svn_fs_root_t root) -> svn_boolean_t"""
    return apply(_fs.svn_fs_is_txn_root, args)

def svn_fs_is_revision_root(*args):
    """svn_fs_is_revision_root(svn_fs_root_t root) -> svn_boolean_t"""
    return apply(_fs.svn_fs_is_revision_root, args)

def svn_fs_txn_root_name(*args):
    """svn_fs_txn_root_name(svn_fs_root_t root, apr_pool_t pool) -> char"""
    return apply(_fs.svn_fs_txn_root_name, args)

def svn_fs_revision_root_revision(*args):
    """svn_fs_revision_root_revision(svn_fs_root_t root) -> svn_revnum_t"""
    return apply(_fs.svn_fs_revision_root_revision, args)
svn_fs_path_change_modify = _fs.svn_fs_path_change_modify
svn_fs_path_change_add = _fs.svn_fs_path_change_add
svn_fs_path_change_delete = _fs.svn_fs_path_change_delete
svn_fs_path_change_replace = _fs.svn_fs_path_change_replace
svn_fs_path_change_reset = _fs.svn_fs_path_change_reset
class svn_fs_path_change_t:
    """Proxy of C svn_fs_path_change_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_fs_path_change_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_fs_path_change_t, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C svn_fs_path_change_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["node_rev_id"] = _fs.svn_fs_path_change_t_node_rev_id_set
    __swig_getmethods__["node_rev_id"] = _fs.svn_fs_path_change_t_node_rev_id_get
    __swig_setmethods__["change_kind"] = _fs.svn_fs_path_change_t_change_kind_set
    __swig_getmethods__["change_kind"] = _fs.svn_fs_path_change_t_change_kind_get
    __swig_setmethods__["text_mod"] = _fs.svn_fs_path_change_t_text_mod_set
    __swig_getmethods__["text_mod"] = _fs.svn_fs_path_change_t_text_mod_get
    __swig_setmethods__["prop_mod"] = _fs.svn_fs_path_change_t_prop_mod_set
    __swig_getmethods__["prop_mod"] = _fs.svn_fs_path_change_t_prop_mod_get
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_fs_path_change_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)


class svn_fs_path_change_tPtr(svn_fs_path_change_t):
    def __init__(self, this):
        _swig_setattr(self, svn_fs_path_change_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_fs_path_change_t, 'thisown', 0)
        _swig_setattr(self, svn_fs_path_change_t,self.__class__,svn_fs_path_change_t)
_fs.svn_fs_path_change_t_swigregister(svn_fs_path_change_tPtr)


def svn_fs_paths_changed(*args):
    """svn_fs_paths_changed(apr_hash_t changed_paths_p, svn_fs_root_t root, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_paths_changed, args)

def svn_fs_check_path(*args):
    """
    svn_fs_check_path(svn_node_kind_t kind_p, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_check_path, args)

def svn_fs_node_history(*args):
    """
    svn_fs_node_history(svn_fs_history_t history_p, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_node_history, args)

def svn_fs_history_prev(*args):
    """
    svn_fs_history_prev(svn_fs_history_t prev_history_p, svn_fs_history_t history, 
        svn_boolean_t cross_copies, apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_history_prev, args)

def svn_fs_history_location(*args):
    """
    svn_fs_history_location(char path, svn_revnum_t revision, svn_fs_history_t history, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_history_location, args)

def svn_fs_is_dir(*args):
    """
    svn_fs_is_dir(svn_boolean_t is_dir, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_is_dir, args)

def svn_fs_is_file(*args):
    """
    svn_fs_is_file(svn_boolean_t is_file, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_is_file, args)

def svn_fs_node_id(*args):
    """svn_fs_node_id(svn_fs_id_t id_p, svn_fs_root_t root, char path, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_node_id, args)

def svn_fs_node_created_rev(*args):
    """
    svn_fs_node_created_rev(svn_revnum_t revision, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_node_created_rev, args)

def svn_fs_node_created_path(*args):
    """svn_fs_node_created_path(char created_path, svn_fs_root_t root, char path, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_node_created_path, args)

def svn_fs_node_prop(*args):
    """
    svn_fs_node_prop(svn_string_t value_p, svn_fs_root_t root, char path, 
        char propname, apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_node_prop, args)

def svn_fs_node_proplist(*args):
    """
    svn_fs_node_proplist(apr_hash_t table_p, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_node_proplist, args)

def svn_fs_change_node_prop(*args):
    """
    svn_fs_change_node_prop(svn_fs_root_t root, char path, char name, svn_string_t value, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_change_node_prop, args)

def svn_fs_props_changed(*args):
    """
    svn_fs_props_changed(svn_boolean_t changed_p, svn_fs_root_t root1, char path1, 
        svn_fs_root_t root2, char path2, apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_props_changed, args)

def svn_fs_copied_from(*args):
    """
    svn_fs_copied_from(svn_revnum_t rev_p, char path_p, svn_fs_root_t root, 
        char path, apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_copied_from, args)

def svn_fs_closest_copy(*args):
    """
    svn_fs_closest_copy(svn_fs_root_t root_p, char path_p, svn_fs_root_t root, 
        char path, apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_closest_copy, args)

def svn_fs_merge(*args):
    """
    svn_fs_merge(char conflict_p, svn_fs_root_t source_root, char source_path, 
        svn_fs_root_t target_root, char target_path, 
        svn_fs_root_t ancestor_root, char ancestor_path, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_merge, args)
class svn_fs_dirent_t:
    """Proxy of C svn_fs_dirent_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_fs_dirent_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_fs_dirent_t, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C svn_fs_dirent_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["name"] = _fs.svn_fs_dirent_t_name_set
    __swig_getmethods__["name"] = _fs.svn_fs_dirent_t_name_get
    __swig_setmethods__["id"] = _fs.svn_fs_dirent_t_id_set
    __swig_getmethods__["id"] = _fs.svn_fs_dirent_t_id_get
    __swig_setmethods__["kind"] = _fs.svn_fs_dirent_t_kind_set
    __swig_getmethods__["kind"] = _fs.svn_fs_dirent_t_kind_get
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_fs_dirent_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)


class svn_fs_dirent_tPtr(svn_fs_dirent_t):
    def __init__(self, this):
        _swig_setattr(self, svn_fs_dirent_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_fs_dirent_t, 'thisown', 0)
        _swig_setattr(self, svn_fs_dirent_t,self.__class__,svn_fs_dirent_t)
_fs.svn_fs_dirent_t_swigregister(svn_fs_dirent_tPtr)


def svn_fs_dir_entries(*args):
    """
    svn_fs_dir_entries(apr_hash_t entries_p, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_dir_entries, args)

def svn_fs_make_dir(*args):
    """svn_fs_make_dir(svn_fs_root_t root, char path, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_make_dir, args)

def svn_fs_delete(*args):
    """svn_fs_delete(svn_fs_root_t root, char path, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_delete, args)

def svn_fs_copy(*args):
    """
    svn_fs_copy(svn_fs_root_t from_root, char from_path, svn_fs_root_t to_root, 
        char to_path, apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_copy, args)

def svn_fs_revision_link(*args):
    """
    svn_fs_revision_link(svn_fs_root_t from_root, svn_fs_root_t to_root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_revision_link, args)

def svn_fs_file_length(*args):
    """
    svn_fs_file_length(svn_filesize_t length_p, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_file_length, args)

def svn_fs_file_md5_checksum(*args):
    """
    svn_fs_file_md5_checksum(unsigned char digest, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_file_md5_checksum, args)

def svn_fs_file_contents(*args):
    """
    svn_fs_file_contents(svn_stream_t contents, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_file_contents, args)

def svn_fs_make_file(*args):
    """svn_fs_make_file(svn_fs_root_t root, char path, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_make_file, args)

def svn_fs_apply_textdelta(*args):
    """
    svn_fs_apply_textdelta(svn_txdelta_window_handler_t contents_p, void contents_baton_p, 
        svn_fs_root_t root, char path, char base_checksum, 
        char result_checksum, apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_apply_textdelta, args)

def svn_fs_apply_text(*args):
    """
    svn_fs_apply_text(svn_stream_t contents_p, svn_fs_root_t root, char path, 
        char result_checksum, apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_apply_text, args)

def svn_fs_contents_changed(*args):
    """
    svn_fs_contents_changed(svn_boolean_t changed_p, svn_fs_root_t root1, char path1, 
        svn_fs_root_t root2, char path2, apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_contents_changed, args)

def svn_fs_youngest_rev(*args):
    """svn_fs_youngest_rev(svn_revnum_t youngest_p, svn_fs_t fs, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_youngest_rev, args)

def svn_fs_deltify_revision(*args):
    """svn_fs_deltify_revision(svn_fs_t fs, svn_revnum_t revision, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_deltify_revision, args)

def svn_fs_revision_prop(*args):
    """
    svn_fs_revision_prop(svn_string_t value_p, svn_fs_t fs, svn_revnum_t rev, 
        char propname, apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_revision_prop, args)

def svn_fs_revision_proplist(*args):
    """
    svn_fs_revision_proplist(apr_hash_t table_p, svn_fs_t fs, svn_revnum_t rev, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_revision_proplist, args)

def svn_fs_change_rev_prop(*args):
    """
    svn_fs_change_rev_prop(svn_fs_t fs, svn_revnum_t rev, char name, svn_string_t value, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_change_rev_prop, args)

def svn_fs_get_file_delta_stream(*args):
    """
    svn_fs_get_file_delta_stream(svn_txdelta_stream_t stream_p, svn_fs_root_t source_root, 
        char source_path, svn_fs_root_t target_root, 
        char target_path, apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_get_file_delta_stream, args)

def svn_fs_get_uuid(*args):
    """svn_fs_get_uuid(svn_fs_t fs, char uuid, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_get_uuid, args)

def svn_fs_set_uuid(*args):
    """svn_fs_set_uuid(svn_fs_t fs, char uuid, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_set_uuid, args)

def svn_fs_lock(*args):
    """
    svn_fs_lock(svn_lock_t lock, svn_fs_t fs, char path, char token, 
        char comment, svn_boolean_t is_dav_comment, 
        apr_time_t expiration_date, svn_revnum_t current_rev, 
        svn_boolean_t steal_lock, apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_lock, args)

def svn_fs_generate_lock_token(*args):
    """svn_fs_generate_lock_token(char token, svn_fs_t fs, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_generate_lock_token, args)

def svn_fs_unlock(*args):
    """
    svn_fs_unlock(svn_fs_t fs, char path, char token, svn_boolean_t break_lock, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_unlock, args)

def svn_fs_get_lock(*args):
    """svn_fs_get_lock(svn_lock_t lock, svn_fs_t fs, char path, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_get_lock, args)

def svn_fs_get_locks(*args):
    """
    svn_fs_get_locks(svn_fs_t fs, char path, svn_fs_get_locks_callback_t get_locks_func, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_fs.svn_fs_get_locks, args)

def svn_fs_print_modules(*args):
    """svn_fs_print_modules(svn_stringbuf_t output, apr_pool_t pool) -> svn_error_t"""
    return apply(_fs.svn_fs_print_modules, args)
class svn_fs_t:
    """Proxy of C svn_fs_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_fs_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_fs_t, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C svn_fs_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_fs_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)


class svn_fs_tPtr(svn_fs_t):
    def __init__(self, this):
        _swig_setattr(self, svn_fs_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_fs_t, 'thisown', 0)
        _swig_setattr(self, svn_fs_t,self.__class__,svn_fs_t)
_fs.svn_fs_t_swigregister(svn_fs_tPtr)

class svn_fs_access_t:
    """Proxy of C svn_fs_access_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_fs_access_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_fs_access_t, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C svn_fs_access_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_fs_access_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)


class svn_fs_access_tPtr(svn_fs_access_t):
    def __init__(self, this):
        _swig_setattr(self, svn_fs_access_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_fs_access_t, 'thisown', 0)
        _swig_setattr(self, svn_fs_access_t,self.__class__,svn_fs_access_t)
_fs.svn_fs_access_t_swigregister(svn_fs_access_tPtr)

class svn_fs_id_t:
    """Proxy of C svn_fs_id_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_fs_id_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_fs_id_t, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C svn_fs_id_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_fs_id_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)


class svn_fs_id_tPtr(svn_fs_id_t):
    def __init__(self, this):
        _swig_setattr(self, svn_fs_id_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_fs_id_t, 'thisown', 0)
        _swig_setattr(self, svn_fs_id_t,self.__class__,svn_fs_id_t)
_fs.svn_fs_id_t_swigregister(svn_fs_id_tPtr)

class svn_fs_txn_t:
    """Proxy of C svn_fs_txn_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_fs_txn_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_fs_txn_t, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C svn_fs_txn_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_fs_txn_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)


class svn_fs_txn_tPtr(svn_fs_txn_t):
    def __init__(self, this):
        _swig_setattr(self, svn_fs_txn_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_fs_txn_t, 'thisown', 0)
        _swig_setattr(self, svn_fs_txn_t,self.__class__,svn_fs_txn_t)
_fs.svn_fs_txn_t_swigregister(svn_fs_txn_tPtr)

class svn_fs_root_t:
    """Proxy of C svn_fs_root_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_fs_root_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_fs_root_t, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C svn_fs_root_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_fs_root_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)


class svn_fs_root_tPtr(svn_fs_root_t):
    def __init__(self, this):
        _swig_setattr(self, svn_fs_root_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_fs_root_t, 'thisown', 0)
        _swig_setattr(self, svn_fs_root_t,self.__class__,svn_fs_root_t)
_fs.svn_fs_root_t_swigregister(svn_fs_root_tPtr)

class svn_fs_history_t:
    """Proxy of C svn_fs_history_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_fs_history_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_fs_history_t, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C svn_fs_history_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_fs_history_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)


class svn_fs_history_tPtr(svn_fs_history_t):
    def __init__(self, this):
        _swig_setattr(self, svn_fs_history_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_fs_history_t, 'thisown', 0)
        _swig_setattr(self, svn_fs_history_t,self.__class__,svn_fs_history_t)
_fs.svn_fs_history_t_swigregister(svn_fs_history_tPtr)


