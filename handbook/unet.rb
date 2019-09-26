# -*- coding: utf-8 -*- #
# frozen_string_literal: true

module Rouge
  module Lexers
    class Unet < RegexLexer
      title "Unet"
      desc 'Unet shell session'
      tag 'unet'

      state :root do
        rule %r(^\w+ >> .*$), Generic::Heading
        rule %r(^(?!> )(?!\-  )(?!\- \}).*$), Generic::Output
        rule %r(//.*$), Comment::Single
        rule %r(^[>\-] ), Generic::Prompt
        rule %r(import\b), Keyword::Namespace
        rule %r(new\b), Keyword::Reserved
        rule %r/"(\\.|\\\n|.)*?"/, Str::Double
        rule %r/'(\\.|\\\n|.)*?'/, Str::Single
        rule %r/\d+\.\d+([eE]\d+)?[fd]?/, Num::Float
        rule %r/0x[0-9a-f]+/, Num::Hex
        rule %r/[0-9]+L?/, Num::Integer
        rule %r(\n), Text::Whitespace
        rule %r(\w+), Generic::Strong
        rule %r(.), Generic::Strong
      end

    end
  end
end
