;;; Directory Local Variables for a Python project -*- no-byte-compile: t; -*-
;; Author: James Cherti
;; License: MIT
;; URL: https://www.jamescherti.com/emacs-eglot-python-dir-locals-el-and-pylsp/
;;
;; Requires:
;;   - python-lsp-server: https://github.com/python-lsp/python-lsp-server
;;   - Checkers:
;;       - ruff: https://github.com/astral-sh/ruff
;;       - pylint: https://github.com/pylint-dev/pylint
;;   - Pylsp Plugins:
;;     - python-lsp-ruff: https://github.com/python-lsp/python-lsp-ruff
;;     - pylsp-mypy: https://github.com/python-lsp/pylsp-mypy
;;
;; Documentation:
;;   - https://github.com/python-lsp/python-lsp-server/blob/develop/CONFIGURATION.md
;;   - https://github.com/python-lsp/python-lsp-ruff
;;   - https://github.com/chantera/python-lsp-isort

((nil . ((sentence-end-double-space . nil)
         (require-final-newline . t)))
 (python-base-mode
  . ((indent-tabs-mode . nil)
     (tab-width . 4)
     (fill-column . 88)
     (python-indent-offset . 4)
     (python-indent-guess-indent-offset . nil)
     (eglot-workspace-configuration
      . (:pylsp
         (;; Formatter to use for reformatting signatures in docstrings.
          :signature
          (;; Signature
           :formatter "ruff"
           :include_docstring t
           :line_length 88)
          :plugins
          (:ruff
           (;; Ruff plugin (Requires: ruff and python-lsp-ruff)
            :enabled t
            :formatEnabled t
            :lineLength 88
            ;; I: Sort imports
            :extendSelect ["I"]
            :format ["I"])

           :pylsp_mypy
           (;; Type checking (Requires: pylsp-mypy)
            :enabled t

            ;; Disabling live mode prevents type-checking updates on every edit.
            ;; Save the file to refresh mypy diagnostics.
            :live_mode :json-false

            ;; :dmypy :json-false
            ;; :report_progress t
            )

           :pylint
           (;; Pylint
            :enabled :json-false
            ;; :args []
            )

           :flake8 (:enabled :json-false)
           :mccabe (:enabled :json-false)
           :pyflakes (:enabled :json-false)
           :pycodestyle (:enabled :json-false)
           :pydocstyle (:enabled :json-false)
           :isort (:enabled :json-false)

           :autopep8 (:enabled :json-false)
           :yapf (:enabled :json-false)

           :preload (:enabled :json-false)
           :rope_autoimport (:enabled :json-false)
           :rope_completion (:enabled :json-false)

           :jedi_completion
           (;; Jedi code completion
            :enabled t

            ;; Adds class objects as a separate completion item.
            ;; :include_class_objects t

            ;; Adds function objects as a separate completion item.
            ;; :include_function_objects t

            ;; Auto-completes methods and classes with tabstops for each
            ;; parameter.
            ;; :include_params t

            ;; How many labels and snippets (at most) should be resolved?
            ;; :resolve_at_most 25

            ;; Resolve documentation and detail eagerly.
            ;; :eager :json-false

            ;; Disable fuzzy when requesting autocomplete.
            ;; :fuzzy :json-false
            )

           ;; :jedi
           ;; (;; Uncomment to add custom module paths or pin a virtualenv
           ;;  ;; :extra_paths ["src"]
           ;;  ;; :prioritize_extra_paths t
           ;;  ;; :environment ".venv"
           ;;  :auto_import_modules ["numpy"])

           ;; :jedi_definition
           ;; (;; Jedi definition
           ;;  :enabled t
           ;;  :follow_imports t
           ;;  :follow_builtin_imports t
           ;;  :follow_builtin_definitions t)

           ;; :jedi_type_definition (:enabled t)
           ;; :jedi_hover (:enabled t)
           ;; :jedi_references (:enabled t)
           ;; :jedi_signature_help (:enabled t)
           ;; :jedi_symbols
           ;; (:enabled t
           ;;           :all_scopes t
           ;;           :include_import_symbols t)
           )))))))
