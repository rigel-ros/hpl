from .ast import (
    HplArrayAccess,
    HplAstObject,
    HplBinaryOperator,
    HplContradiction,
    HplEvent,
    HplEventDisjunction,
    HplExpression,
    HplFieldAccess,
    HplFunctionCall,
    HplLiteral,
    HplPattern,
    HplPredicate,
    HplProperty,
    HplQuantifier,
    HplRange,
    HplScope,
    HplSet,
    HplSimpleEvent,
    HplSpecification,
    HplThisMessage,
    HplUnaryOperator,
    HplVacuousTruth,
    HplValue,
    HplVarReference
)
from typing import Protocol


class HplAstVisitor(Protocol):
    """
    This class specifies the interface all visitor instances must adhere to.
    """

    def visit_hpl_array_access(self, node: HplArrayAccess) -> None:
        """
        Use this function to visit nodes of type HplArrayAccess.
        """
        ...

    def visit_hpl_ast_object(self, node: HplAstObject) -> None:
        """
        Use this function to visit nodes of type HplAstObject.
        """
        ...

    def visit_hpl_binary_operator(self, node: HplBinaryOperator) -> None:
        """
        Use this function to visit nodes of type HplBinaryOperator.
        """
        ...

    def visit_hpl_contradiction(self, node: HplContradiction) -> None:
        """
        Use this function to visit nodes of type HplContradiction.
        """
        ...

    def visit_hpl_event(self, node: HplEvent) -> None:
        """
        Use this function to visit nodes of type HplEvent.
        """
        ...

    def visit_hpl_event_disjunction(self, node: HplEventDisjunction) -> None:
        """
        Use this function to visit nodes of type HplEventDisjunction.
        """
        ...

    def visit_hpl_expression(self, node: HplPattern) -> None:
        """
        Use this function to visit nodes of type HplPattern.
        """
        ...

    def visit_hpl_field_access(self, node: HplFieldAccess) -> None:
        """
        Use this function to visit nodes of type HplFieldAccess.
        """
        ...

    def visit_hpl_functional_call(self, node: HplFunctionCall) -> None:
        """
        Use this function to visit nodes of type HplFunctionCall.
        """
        ...

    def visit_hpl_literal(self, node: HplLiteral) -> None:
        """
        Use this function to visit nodes of type HplLiteral.
        """
        ...

    def visit_hpl_pattern(self, node: HplExpression) -> None:
        """
        Use this function to visit nodes of type HplExpression.
        """
        ...

    def visit_hpl_predicate(self, node: HplPredicate) -> None:
        """
        Use this function to visit nodes of type HplPredicate.
        """
        ...

    def visit_hpl_property(self, node: HplProperty) -> None:
        """
        Use this function to visit nodes of type HplProperty.
        """
        ...

    def visit_hpl_quantifier(self, node: HplQuantifier) -> None:
        """
        Use this function to visit nodes of type HplQuantifier.
        """
        ...

    def visit_hpl_range(self, node: HplRange) -> None:
        """
        Use this function to visit nodes of type HplRange.
        """
        ...

    def visit_hpl_scope(self, node: HplScope) -> None:
        """
        Use this function to visit nodes of type HplScope.
        """
        ...

    def visit_hpl_set(self, node: HplSet) -> None:
        """
        Use this function to visit nodes of type HplSet.
        """
        ...

    def visit_hpl_simple_event(self, node: HplSimpleEvent) -> None:
        """
        Use this function to visit nodes of type HplSimpleEvent.
        """
        ...

    def visit_hpl_specification(self, node: HplSpecification) -> None:
        """
        Use this function to visit nodes of type HplSpecification.
        """
        ...

    def visit_hpl_this_message(self, node: HplThisMessage) -> None:
        """
        Use this function to visit nodes of type HplThisMessage.
        """
        ...

    def visit_hpl_unary_operator(self, node: HplUnaryOperator) -> None:
        """
        Use this function to visit nodes of type HplUnaryOperator.
        """
        ...

    def visit_hpl_vacuous_truth(self, node: HplVacuousTruth) -> None:
        """
        Use this function to visit nodes of type HplVacuousTruth.
        """
        ...

    def visit_hpl_value(self, node: HplValue) -> None:
        """
        Use this function to visit nodes of type HplValue.
        """
        ...

    def visit_hpl_var_reference(self, node: HplVarReference) -> None:
        """
        Use this function to visit nodes of type HplVarReference.
        """
        ...
